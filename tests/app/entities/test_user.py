import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:
    def test_user(self):
        user = User(name="Carlos", agency="9999", account="11111-1", current_balance=500000.0)
        assert user.name == "Carlos"
        assert user.agency == "9999"
        assert user.account == "11111-1"
        assert user.current_balance == 500000.0
        assert user.to_dict() == {
            "name": "Carlos",
            "agency": "9999",
            "account": "11111-1",
            "current_balance": 500000.0
        }

    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name= 500000.0, agency="9999", account="11111-1", current_balance=500000.0)
  
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name=None, agency="9999", account="11111-1", current_balance=500000.0)

    def test_user_agency_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name= "Carlos", agency= 50.0, account="11111-1", current_balance=500000.0)
    
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency=None, account="11111-1", current_balance=500000.0)

    def test_user_agency_is_not_4_digits(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="999", account="11111-1", current_balance=500000.0)

    def test_user_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name= "Carlos", agency= "9999", account= 500000.0, current_balance=500000.0)
    
    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="9999", account=None, current_balance=500000.0)

    def test_user_account_is_not_7_digits(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="9999", account="1111-1", current_balance=500000.0)

    def test_user_account_is_not_in_format(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="9999", account="111111", current_balance=500000.0)
    
    def test_user_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="9999", account="11111-1", current_balance=500000)
            
    def test_user_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Carlos", agency="9999", account="11111-1", current_balance=None)
            

