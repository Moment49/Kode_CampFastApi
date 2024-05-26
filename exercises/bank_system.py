import maskpass
import json
# A basic Banking system
def Main():
    # Create a login Page for 
    filename = "user_accounts.json"
    Users_accounts = {}
    active = True
    while active:
        main_prompt = "Basic Banking System"
        main_prompt += "\n1 - Login to Account"
        main_prompt += "\n2 - Exit Application"
        main_prompt += "\nPlease select either 1 or 2 to proceed: "

        user_res = input(main_prompt)

        # Check condition:
        if user_res == '2':
            print("Application Closed!!!")
            active = False
        elif user_res == '1':
            print("======= Login Page =======")
            isloggedIn = False
            while not isloggedIn:
                user_name = input("Enter username: ")
                # Using the maskpass() to hide user password
                user_pass = maskpass.askpass(prompt="Enter pasword: ", mask="*")

                if user_name == 'Momentum' and user_pass == 'admin':
                    active = False
                    isloggedIn = True
                
                    print(f"\nWelcome - {user_name}\n")
                    log_prompt = "1 - Deposit Funds"
                    log_prompt += "\n2 - Withdraw Funds"
                    log_prompt += "\n3 - Check Balance"
                    log_prompt += "\nPlease select any to proceed: "
                    user_opt = input(log_prompt)
                    with open(filename, 'r') as f:
                        accounts = json.load(f)
                        # print(accounts)
                    if user_opt == "1":
                        while user_opt:
                            print("\n===== Make Deposit ======")
                            user_account_no = input("Enter acccount number: ")
                            for user_acc_no, user_amt in accounts.items():
                                if user_account_no == user_acc_no:
                                    # Check if the account number exist in the json file
                                    depo_amount = int(input("Enter an amount to deposit: "))
                                    depo_amount += user_amt
                                    Users_accounts[user_account_no] = depo_amount 
                                    with open(filename, 'w') as f:
                                        json.dump(Users_accounts, f)
                                    print(f"Funds deposited: ${depo_amount}")
                                else:
                                    # Make a fresh deposit to account
                                    depo_amount = int(input("Enter an amount to deposit: "))
                                    Users_accounts[user_account_no] = depo_amount 
                                    with open(filename, 'w') as f:
                                        json.dump(Users_accounts, f)
                                    print(f"Funds deposited: ${depo_amount}")

                            user_res = input("Do you want to make another deposit (yes or no): ")
                            if user_res.lower() == 'no':
                                print("Logged out")
                                isloggedIn = True
                                break
                    elif user_opt == "2":
                        print("\n===== Withdraw Funds ======")
                        while user_opt:
                            user_acct_no = input("Enter account number: ")
                            for user_account_no, user_amt in accounts.items():
                                if user_acct_no == user_account_no:
                                    withdraw_amt = int(input("Enter amount to withdraw: "))
                                    user_amt -= withdraw_amt
                                    print(f"You have withdrawn: ${withdraw_amt}")
                                    Users_accounts[user_account_no] = user_amt
                                    # Update the json file with the appropriate funds
                                    with open(filename, 'w') as f:
                                        json.dump(Users_accounts, f)
                            user_res = input("Do you want to make another withdrawal (yes or no): ")
                            if user_res.lower() == 'no':
                                print("Logged out")
                                isloggedIn = True
                                break
                    elif user_opt == "3":
                        user_acct_no = input("Enter account number: ")
                        print("===== Account Balance ======")
                        for user_account_no, user_amt in accounts.items():
                            if user_acct_no == user_account_no:
                                print(f"Account Number: {user_acct_no}")
                                print(f"Amount: {user_amt}")
                    else:
                        print("Invalid account details")

if __name__ == '__main__':
    Main()