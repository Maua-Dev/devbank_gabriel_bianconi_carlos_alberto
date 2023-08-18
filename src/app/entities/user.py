from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: str 
    account: str 
    current_balance: float
    
    def __init__(self,name = None, agency = None, account = None, current_balance = None):
        
        validate_name = self.validate_name(name)
        if validate_name[0] is False:
            raise ParamNotValidated('name', validate_name[1])
        self.name = name
        
        validate_agency = self.validate_agency(agency)
        if validate_agency[0] is False:
            raise ParamNotValidated('agency', validate_agency[1])
        self.agency = agency
        
        validate_account = self.validate_account(account)
        if validate_account[0] is False:
            raise ParamNotValidated('account', validate_account[1])
        self.account = account
        
        validate_current_balance = self.validate_current_balance(current_balance)
        if validate_current_balance[0] is False:
            raise ParamNotValidated('current_balance', validate_current_balance[1])
        self.current_balance = current_balance
        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return False, "Name is required"
        if type(name) != str:
            return False, "Name must be a string"
        if len(name) < 3:
            return False, "Name must be at least 3 characters long"
        return True, ""

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return False, "Agency is required"
        if type(agency) != str:
            return False, "Agency must be a string"
        if len(agency) != 4:
            return False, "Agency must be 4 characters long"
        return True, ""

    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return False, "Account is required"
        if type(account) != str:
            return False, "Account must be a string"
        if len(account) != 7:
            return False, "Account must be 7 characters long"
        if account[5] != "-":
            return False, "Account must be in the format XXXXX-X"
        return True, ""

    @staticmethod
    def validate_current_balance(balance: float) -> Tuple[bool, str]:
        if balance is None:
            return False, "Balance is required"
        if type(balance) != float:
            return False, "Balance must be a float"
        if balance < 0:
            return False, "Balance must be a positive number"
        return True, ""
    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }