import pytest
from src.app.entities.transactions import Transaction
from src.app.enums.Transaction_Type_Enum import TRANSACTIONTYPEENUM
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(type_transactions=TRANSACTIONTYPEENUM.DEPOSIT, value=2000.0, current_balance=2000.0)
        assert transaction.type == TRANSACTIONTYPEENUM.DEPOSIT
        assert transaction.value == 2000.0
        assert transaction.current_balance == 2000.0
        assert transaction.timestamp is not None

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions="deposit", value=2000.0, current_balance=2000.0)
            
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=None, value=2000.0, current_balance=2000.0)

    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTIONTYPEENUM.DEPOSIT, value="100.0", current_balance=2000.0)
            
    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTIONTYPEENUM.DEPOSIT, value=None, current_balance=2000.0)
            
    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTIONTYPEENUM.DEPOSIT, value=100.0, current_balance="2000.0")
            
    def test_transaction_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTIONTYPEENUM.DEPOSIT, value=100.0, current_balance=None)
            
    
            
            