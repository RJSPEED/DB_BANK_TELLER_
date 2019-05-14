
def show_menu():
    print()
    print("Welcome to Terminal Teller!:")
    print()
    print("[1] Create Account")
    print()
    print("[2] Log In")
    print()
    print("[3] Exit")
    print()

def get_input():
    print()
    print("Your choice: ", end="")
    return input()

def get_input_new_account(param):
    print()
    print("Account Creation:")
    print()
    print(param, " : ", end="")
    return input()

def get_new_account_confirm(account):
    print()
    print("Account created, your account number is: ", account)
    print()

def get_pins_unmatched():
    print()
    print("The PIN and Confirm PIN values do not match, pls retry.")
    print()

def get_account_details(param):
    print()
    print(param, " : ", end="")
    return input()

def get_login_greeting(details):
    print()
    print("Hello: ", details)
    print()

def get_failed_validate_msg():
    print()
    print("Failed to find an account for the given account and pin details, pls retry. ")
    print()

def show_op2_menu():
    print()
    print("[1] Check Balance")
    print()
    print("[2] Withdraw Funds")
    print()
    print("[3] Deposit Funds")
    print()
    print("[4] Sign Out")
    print()

def get_with_or_dep_amount(param):
    print()
    print(param, " ", end="")
    return input()

def get_show_balance(balance):
    print()
    print("Your balance is: £", float(balance))
    print()

def get_post_withdrawal_reject_msg():
    print()
    print("Insufficient funds, pls enter a smaller amount")
    print()

def get_post_withdrawal_msg(amount,balance):
    print()
    print("You have just withdrawn: £", float(amount))
    print()
    print("Your new balance is: £", float(balance))
    print()

def get_post_deposit_msg(amount,balance):
    print()
    print("You have just deposited: £", float(amount))
    print()
    print("Your new balance is: £", float(balance))
    print()








def get_grade():
    print()
    print("Input the new grade: ", end="")
    return int(input())

def show_gpa(gpa):
    print()
    print("Student's GPA is {}.".format(gpa))
