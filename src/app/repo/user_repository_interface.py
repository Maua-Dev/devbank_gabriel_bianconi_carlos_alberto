from abc import ABC, abstractmethod
from typing import List

from ..entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> List[User]:
        """
        Returns user in the database
        """
        pass

    @abstractmethod
    def withdraw_current_balance(self, current_balance:float) -> float:
        
        """
        Updates the balance with the given id.
        If the balance does not exist, returns None
        """
        pass
    @abstractmethod
    def deposit_current_balance(self, current_balance:float) -> float:
        
        """
        Updates the balance with the given id.
        If the balance does not exist, returns None
        """  
        pass