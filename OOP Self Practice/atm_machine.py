import numpy as np
import secrets


class Atm:

    def __init__(self) -> None:
        self._pin: int = None
        self._accountno: int = None
        self._accountbalance: int = 0
        self.__menu()

    def __menu(self) -> None:
        while True:
            try:
                user_input: int = int(input(self.menu_options()))
                options = {
                    1: self.create_pin,
                    2: self.create_accountno,
                    3: self.withdraw_balance,
                    4: self.deposit_balance,
                    5: self.get_details,
                }

                if user_input in options and user_input != 6:
                    print(options[user_input]())
                elif user_input == 6:
                    break
                else:
                    print("please try to input number in between range")
            except ValueError:
                print("Please input number not string type")

    def security_check(self, input_message: str, expected_value: int) -> bool:
        while True:
            try:
                user_input = int(input(input_message))
                if user_input == expected_value:
                    return True
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Enter a valid number.")

    def create_pin(self) -> str:
        self._pin = sum(secrets.randbelow(10) for _ in range(3))
        return f"Your pin has been created {self._pin}"

    def create_accountno(self) -> str:
        self._accountno = sum(secrets.randbelow(100) for _ in range(5))
        return f"Your account no has been created {self._accountno}"

    def deposit_balance(self) -> str:
        if self.security_check("Enter your pin: ", self._pin):
            while True:
                try:
                    amount = int(input("Enter your deposit amount: "))
                    if amount > 0:
                        self._accountbalance += amount
                        return f"Deposited successfully, total balance: {self._accountbalance}"
                    else:
                        print("Enter valid amount")
                except ValueError:
                    print("please input valid number")

    def withdraw_balance(self) -> str:
        if self.security_check("Enter your pin: ", self._pin):
            while True:
                try:
                    amount = int(input("Enter your withdraw amount: "))
                    if self._accountbalance >= amount:
                        self._accountbalance -= amount
                        return f"Withdrawn successfully, total balance left: {self._accountbalance}"
                    else:
                        print("Insufficient balance")
                except ValueError:
                    print("please input valid number")

    def get_details(self) -> str:
        if self.security_check("Enter your pin: ", self._pin):
            return f"Pin number: {self._pin} and Account number: {self._accountno} and Balance: {self._accountbalance}"

    def menu_options(self) -> str:
        return """ 
                1.Enter 1 to create a pin number
                2.Enter 2 to create an account number
                3.Enter 3 to withdraw balance
                4.Enter 4 to deposit balance
                5.Enter 5 to get details
                6.Enter 6 to quit application\n"""


hdfc = Atm()
