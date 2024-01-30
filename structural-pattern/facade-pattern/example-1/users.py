from decimal import Decimal

from reports import Reports
from wallets import Wallets


class Users:
    _users: dict[str, dict[str, str]] = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_user(cls, new_user: dict[str, str]) -> str:
        if new_user["user_name"] not in cls._users:
            # generate really complicated unique user_id.
            # Using the existing user_name as the id for simplicity
            user_id = new_user["user_name"]
            cls._users[user_id] = new_user
            Reports.log_event(f"new user `{user_id}` created")
            # create a wallet for the new user
            Wallets().create_wallet(user_id)
            # give the user a sign up bonus
            Reports.log_event(f"Give new user `{user_id}` sign up bonus of 10")
            Wallets().adjust_balance(user_id, Decimal(10))
            return user_id
        return ""

    @classmethod
    def edit_user(cls, user_id: str, user: dict):
        "do nothing"
        print(user_id, user)
        return False

    @classmethod
    def change_pwd(cls, user_id: str, password: str):
        "do nothing"
        print(user_id)
        print(password)
        return False
