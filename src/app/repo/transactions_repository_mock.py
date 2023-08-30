from typing import List
from src.app.entities.transactions import Transaction
from src.app.repo.transactions_repository_interface import ITransactionsRepository
from src.app.enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
import time

class TransactionRepositoryMock(ITransactionsRepository):
    transactions_list : List[Transaction]
    
    def __init__(self):
        self.transactions_list = [
             Transaction(TRANSACTIONTYPEENUM.DEPOSIT, 100.00, 1000.00, time.time()),
             Transaction(TRANSACTIONTYPEENUM.WITHDRAW, 300.00, 700.00, time.time()),
             Transaction(TRANSACTIONTYPEENUM.DEPOSIT, 10.00, 710.00, time.time()),
             Transaction(TRANSACTIONTYPEENUM.WITHDRAW, 30.00, 680.00, time.time()),
             
        ]
        
    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions_list
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions_list.append(transaction)
        return transaction
        
        
    
    
        