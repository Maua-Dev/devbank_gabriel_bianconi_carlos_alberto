import pytest
import time
from src.app.entities.transactions import Transaction
from src.app.enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
from src.app.repo.transactions_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:
    
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        assert all([transaction_expect == transaction for transaction_expect, transaction in zip(repo.transactions.values(), repo.get_all_transactions())])
    
    
    def test_create_transaction_deposit(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(TRANSACTIONTYPEENUM.DEPOSIT, 100.00, 200.00, time.time())
        repo.create_transaction(transaction)
        assert transaction == repo.transactions[len(repo.transactions)]
        
    def test_create_transaction_withdrawn(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(TRANSACTIONTYPEENUM.WITHDRAW, 100.00, 150.00, time.time())
        repo.create_transaction(transaction)
        assert transaction == repo.transactions[len(repo.transactions)]
        