import db_bt_model
import db_bt_view


def run():
    #Call Class method to load sqlite data 
    #db_bt_model.Account.load_datafile()
    mainmenu()

# TODO define separate login function
def login():
    pass

def mainmenu():
    while True:
        db_bt_view.show_menu()
        selection = db_bt_view.get_input()        
        #Account Creation
        if selection == '1':
           #Gather account details
            f_name = db_bt_view.get_input_new_account("First Name")
            l_name = db_bt_view.get_input_new_account("Last Name")
            pin = db_bt_view.get_input_new_account("PIN")
            con_pin = db_bt_view.get_input_new_account("Confirm PIN")
            #Check if pins match
            if pin != con_pin:
                db_bt_view.get_pins_unmatched()
            else:
                #Create account object, pass f_name, l_name, pin
                new_account = db_bt_model.Account("", pin, "", f_name, l_name)
                #Call instance method 'create_account'
                db_bt_view.get_new_account_confirm(new_account.create_account())
        #Log In
        elif selection == '2':    
            #Gather account number and pin
            account = db_bt_view.get_account_details("Account Number")
            pin = db_bt_view.get_account_details("PIN")
            #NEW: Create account object, pass account & pin
            val_account = db_bt_model.Account(account, pin, "", "", "")
            #Call instance method 'validate'
            if not val_account.validate():
                #Failed to find account
                pass
                #db_bt_view.get_failed_validate_msg()
            else:
                #Create account object, pass account
                #load_account = db_bt_model.Account(account, "", "", "", "")
                #Call instance method 'validate'
                #db_bt_view.get_login_greeting(load_account.load_account_data())
                pass
                while True:
                    #New sub-menu
                    db_bt_view.show_op2_menu()
                    op2_selection = db_bt_view.get_input() 
                    if op2_selection == '1':
                        #Check Bal
                        #Call instance method 'get_bal' to retrieve bal for load_account object
                        db_bt_view.get_show_balance(load_account.get_bal())
                    elif op2_selection == '2':
                        #Withdraw
                        amount = db_bt_view.get_with_or_dep_amount("Withdrawal Amount:")
                        #Call instance method 'withdraw' to deduct from bal for load_account object
                        withdraw_response = load_account.withdraw(amount)
                        if not withdraw_response:
                            #Insufficient funds
                            db_bt_view.get_post_withdrawal_reject_msg()
                        else:
                            db_bt_view.get_post_withdrawal_msg(amount, withdraw_response)
                    elif op2_selection == '3':
                        #Deposit
                        amount = db_bt_view.get_with_or_dep_amount("Deposit Amount:")
                        #Call instance method 'deposit' to add to bal for load_account object
                        db_bt_view.get_post_deposit_msg(amount, load_account.deposit(amount))                        
                    else:
                        #Call Class method to save to json file 
                        db_bt_model.Account.save_datafile()
                        return
        else:
            #Call Class method to save to json file 
            db_bt_model.Account.save_datafile()
            return

if __name__ == "__main__":
    run()