import pytest
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.main import get_user, get_history, deposit, withdraw


class Test_Main:
    def test_get_user(self):
        response = get_user()
        expected_response = {
            'name': 'Vitor Soller',
            'agency': '0000',
            'account': '00000-0',
            'current_balance':1000.00
        }
    
        assert response == expected_response

    def test_get_history(self):
        response = get_history()
        assert type(response) == dict
    
    def test_withdraw(self):
        dict_values={
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        }
        response = withdraw(dict_values)
        assert response["current_balance"] == 613.00
        
    # def test_deposit(self):
    #     dict_values={
    #         "2": 1,
    #         "5": 1,
    #         "10": 1,
    #         "20": 1,
    #         "50": 1,
    #         "100": 1,
    #         "200": 1
    #     }
    #     response = deposit(dict_values)
    #     assert response["current_balance"] == 1387.00
        
    