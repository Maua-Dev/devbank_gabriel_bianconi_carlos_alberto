from typing import Dict, List
from src.app.entities.transactions import Transaction
from src.app.repo.transactions_repository_interface import IITransactionsRepository
from src.app.enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
import time

class TransactionRepositoryMock(IITransactionsRepository):
    transactions : List[Transaction]
    
    def __init__(self):
        self.transactions = {
            1: Transaction(TRANSACTIONTYPEENUM.WITHDRAW, 100.00, 150.00, time.time()),
            2: Transaction(TRANSACTIONTYPEENUM.DEPOSIT, 100.00, 200.00, time.time()),
        }
        
    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions.values()
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions[len(self.transactions) + 1] = transaction
        return transaction
        
        
    
    
        