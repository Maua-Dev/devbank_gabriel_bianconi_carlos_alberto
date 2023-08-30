from abc import ABC, abstractmethod
from typing import List
from ..entities.transactions import Transaction


class ITransactionsRepository(ABC):
    
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        '''
        Returns all the transactions in the database 
        '''
        pass
    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        '''
        Creates a new transaction in the database
        '''
        pass
    