import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .entities.transactions import Transaction
from .enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
from .environments import Environments

app = FastAPI()
user_repo = Environments.get_user_repo()
transaction_repo = Environments.get_transaction_repo()

@app.get("/")

def get_user():
     user = user_repo.get_user()
     return user.to_dict()
 
@app.post("/deposit")

def deposit(request: dict):
     if request.keys() != {"2","5","10","20","50","100","200"}:
          raise HTTPException(status_code=400, detail="Valor Inválido!")
     
     total_amount = sum(int(key) * value for key,value in request.items())
     
     if total_amount <= 0:
          raise HTTPException(status_code=400, detail="Depósito total deve ser p")
     
     user = user_repo.get_user().to_dict()
     
     if total_amount > 2*user["current_balance"]:
          raise HTTPException(status_code=403, detail="Depósito suspeito")
     
     transaction = Transaction(
          type_transactions = TRANSACTIONTYPEENUM.DEPOSIT,
          value = float(total_amount),
          current_balance = total_amount + user["current_balance"],
          timestamp = time.time()*1000 
     )    

     transaction_repo.create_transaction(transaction)
     user_repo.deposit_current_balance(total_amount)

     return transaction.to_dict()
     
@app.post("/withdraw")

def withdraw(request: dict):
     if request.keys() != {"2","5","10","20","50","100","200"}:
          raise HTTPException(status_code=400, detail="Valor Inválido!")

     total_value = sum(int(key) * value for key,value in request.items())
     user = user_repo.get_user().to_dict()
     if total_value > user["current_balance"]:
          raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")

     transaction = Transaction(
          type_transactions = TRANSACTIONTYPEENUM.WITHDRAW,
          value = float(total_value),
          current_balance = user["current_balance"] - total_value,
          timestamp = time.time()*1000
     )

     transaction_repo.create_transaction(transaction)
     user_repo.withdraw_current_balance(total_value)

     return transaction.to_dict()
 
@app.get("/history")

def get_history():
     transactions = transaction_repo.get_all_transactions()
     history = [transaction.to_dict() for transaction in transactions]
     return {
          'all_transactions':history
     }
     
handler = Mangum(app, lifespan="off")  