from decimal import Decimal

from game_engine import GameEngine
from reports import Reports
from users import Users
from wallets import Wallets


class GameAPI:
    "The Game API facade"

    @staticmethod
    def get_balance(user_id: str):
        return Wallets.get_balance(user_id)

    @staticmethod
    def game_state() -> dict:
        return GameEngine().get_game_state()

    @staticmethod
    def get_history() -> dict:
        return Reports.get_history()

    @staticmethod
    def change_pwd(user_id: str, password: str) -> bool:
        return Users.change_pwd(user_id, password)

    @staticmethod
    def register_user(value: dict[str, str]) -> str:
        "register a new user and returns the new id"
        return Users.register_user(value)
    @staticmethod
    def submit_entry(user_id: str, entry: Decimal) -> bool:
        "submit a bet"
        return GameEngine().submit_entry(user_id, entry)
