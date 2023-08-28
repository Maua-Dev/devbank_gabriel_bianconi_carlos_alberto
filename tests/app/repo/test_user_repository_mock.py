import pytest
from src.app.repo.user_repository_mock import UserRepositoryMock  # Substitua "your_module" pelo caminho real do seu módulo

class Test_UserRepositoryMock:
    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user()
        assert user.name == "Vitor Soller"  
        assert user.agency == "0000"  
        assert user.account == "00000-0"  
        assert user.current_balance == 1000.0  

    def test_deposit_current_balance(self):
        repo = UserRepositoryMock()
        initial_balance = repo.get_user().current_balance
        deposit_amount = 1000.0
        new_balance = repo.deposit_current_balance(deposit_amount)
        assert new_balance == initial_balance + deposit_amount

    def test_withdraw_current_balance(self):
        repo = UserRepositoryMock()
        initial_balance = repo.get_user().current_balance
        withdrawal_amount = 500.0
        new_balance = repo.withdraw_current_balance(withdrawal_amount)
        assert new_balance == initial_balance - withdrawal_amount