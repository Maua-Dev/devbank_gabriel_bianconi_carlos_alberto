import pytest
import time
from src.app.entities.transactions import Transaction
from src.app.enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
from src.app.repo.transactions_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:
    
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        history = repo.get_all_transactions()
        expected_response = repo.transactions_list
        assert expected_response == history
    
    
    def test_create_transaction_deposit(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(TRANSACTIONTYPEENUM.DEPOSIT, 100.00, 200.00, time.time())
        repo.create_transaction(transaction)
        assert transaction == repo.transactions_list[len(repo.transactions_list) - 1]
        
        
    def test_create_transaction_withdrawn(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(TRANSACTIONTYPEENUM.WITHDRAW, 100.00, 150.00, time.time())
        repo.create_transaction(transaction)
        if len(repo.transactions_list) > 0:
            assert transaction == repo.transactions_list[len(repo.transactions_list) - 1]
        else:
            assert transaction == repo.transactions_list[0]
        