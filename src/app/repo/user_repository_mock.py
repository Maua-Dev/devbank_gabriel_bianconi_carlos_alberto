from ..entities.user import User
from .user_repository_interface import IUserRepository
from typing import List

class UserRepositoryMock(IUserRepository):
    user: List[User]

    def __init__(self):
        self.user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)

    def get_user(self) -> User:
        return self.user

    def deposit_current_balance(self, current_balance: float) -> float:
        self.user.current_balance += current_balance
        return self.user.current_balance

    def withdraw_current_balance(self, current_balance: float) -> float:
        self.user.current_balance -= current_balance
        return self.user.current_balance