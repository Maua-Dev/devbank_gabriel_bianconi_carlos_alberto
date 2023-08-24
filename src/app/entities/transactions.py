from time import time
from typing import Tuple
from ..enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
from ..errors.entity_errors import ParamNotValidated

class Transaction:
    type: TRANSACTIONTYPEENUM
    value: float
    current_balance: float
    timestamp: float
    
    def __init__(self, type_transactions: TRANSACTIONTYPEENUM = None, value= None,current_balance = None,timestamp = None):
        validate_type = self.validate_type(type_transactions)
        if validate_type[0] is False:
            raise ParamNotValidated('type', validate_type[1])
        self.type = type_transactions
        
        validate_value = self.validate_value(value)
        if validate_value[0] is False:
            raise ParamNotValidated('value', validate_value[1])
        self.value = value
        
        validate_current_balance = self.validate_current_balance(current_balance)
        if validate_current_balance[0] is False:
            raise ParamNotValidated('current_balance', validate_current_balance[1])
        self.current_balance = current_balance
        
        timestamp = time() * 1000
        validate_timestamp = self.validate_timestamp(timestamp)
        if validate_timestamp[0] is False:
            raise ParamNotValidated('timestamp', validate_timestamp[1])
        self.timestamp = timestamp
        
        
    @staticmethod
    def validate_type(type_transactions: TRANSACTIONTYPEENUM) -> Tuple[bool, str]:
        if type_transactions is None:
            return (False, "Transaction type is required")
        if type(type_transactions) != TRANSACTIONTYPEENUM:
            return (False, "Transaction Type must be a TransactionsTypeEnum")
        return (True, "")

   
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        if value < 0:
            return (False, "Value must be a positive number")
        return (True, "")

   
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a positive number")
        return (True, "")

   
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != float:
            return (False, "Timestamp must be a datetime")
        return (True, "")
    
    def to_dict(self):
        return {
            "type": self.type.value,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }   