import json
import os
import sqlite3

DIR = os.path.dirname(__file__)
DATAFILENAME = "bank_teller.db"  # use your teller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)

class AuthenticationError(Exception):
    pass

class Account:
    #Class attributes
    data_path = DATAPATH
    acc_data = {}

    def __init__(self, account_num="", pin="", balance="", f_name="", l_name=""):
        # populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
        self.f_name = f_name
        self.l_name = l_name 

    @classmethod
    def load_datafile(cls):
        with open(DATAPATH, "r") as file_object:
            cls.acc_data = json.load(file_object)
        
    @classmethod
    def save_datafile(cls):
        with open(DATAPATH, "w") as file_object:
            json.dump(cls.acc_data, file_object, indent=2)

    def create_account(self):        
        #Retrieve the max account_number and add one to it
        int_keys = list(map(int, self.__class__.acc_data.keys()))
        account_number = str(max(int_keys) + 1)
        #Add new account to dict class attribute  
        self.__class__.acc_data[account_number] = {"first_name": self.f_name, 
                                                   "last_name": self.l_name,
                                                   "pin": self.pin, 
                                                   "balance": 0.00}
        return account_number

    def validate(self):
        # return True or False if the account_num and pin is in the datafile
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            
            SQL = "SELECT * FROM accounts WHERE account_number = ? and pin = ?;"
            cursor.execute(SQL, (self.account_num,self.pin))
            result = cursor.fetchone()
            print("result is: ", result)
            if not result:
                return False
            else:
                return True    

    def load_account_data(self):
        with sqlite3.connect(DATAPATH) as connection:
            cursor = connection.cursor()
            
            SQL = "SELECT first_name FROM accounts WHERE account_number = ? and pin = ?;"
            cursor.execute(SQL, (self.account_num,self.pin))
            result = cursor.fetchone()
            return result

    def get_bal(self):
        return float(self.__class__.acc_data[self.account_num]['balance'])

    def deposit(self, amount):
        self.amount = amount
        # increase the balance of this account
        self.__class__.acc_data[self.account_num]['balance'] = \
            float(self.__class__.acc_data[self.account_num]['balance']) + \
            float(self.amount)
        return float(self.__class__.acc_data[self.account_num]['balance'])

    def withdraw(self, amount):
        # decrease the balance of this account
        # raise ValueError if there is insufficient funds or create an
        # InsufficientFunds exception type
        self.amount = amount
        if self.__class__.acc_data[self.account_num]['balance'] - \
            float(self.amount) < 0:
            return False
        else:
            self.__class__.acc_data[self.account_num]['balance'] = \
            float(self.__class__.acc_data[self.account_num]['balance']) - \
            float(self.amount)
            return float(self.__class__.acc_data[self.account_num]['balance'])

    