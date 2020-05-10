import random
import datetime
import time
import re
import os


def banking_system():
    print("Hello!")
    print("What Would you like to do today?")
    print('''
    1. Staff Login
    2.Close App
    ''')


    def check_staff():
        check_username = input("Enter your username: ").lower()
        check_password = input("Enter your password(Password is case-sensitive): ")
        with open('staff.txt') as staff_details:
            array = [word for line in staff_details for word in line.split()]
            if (check_username == array[0] and check_password == array[1]) or (
                    check_username == array[4] and check_password == array[5]):
                print("Login Successfully! Welcome, " + check_username)

            else:
                print("User not found. Please try again")
                check_staff()

        # save user session in a session.txt file
        login_time = str(datetime.datetime.now())
        with open('session.txt', 'w') as session:
            session.write(check_username + ' ' + 'logged in at ' + login_time)

    staff_login = input("type 1 or 2 for the above function: ")

    def selected():
        if staff_login == '1':
            check_staff()
            after_login()

        if staff_login == '2':
            print("Have a nice day!\n")
            exit()

        else:
            print('Invalid selection! Please try again')
            banking_system()

    def after_login():
        print('''Please choose an action to perform
            Type '1' to Create new bank account
            type '2' to Check Account Details
            type '3' to Logout
            ''')

        account_number = ''.join(map(str, [random.randint(0, 9) for numbers in range(0, 10)]))

        staff_action = input('> ')
        if staff_action == '1':
            print("Please supply the correct format for the following...")
    
            while True:        
                account_name = input("Account name(minimum 3 characters): ")
                if len(account_name) < 3:
                    print("Please enter a name atleast 3 char long")
                else:
                    break

            # opening balance must be a number
            valid_balance = False
            while not valid_balance:
                try:
                    opening_balance = float(input("opening_balance: "))
                    valid_balance = True
                    
                except ValueError:
                    print("Invalid value. Enter number")

            # account type: savings or current
            while True:
                account_type = input("Account Type (s/c): ").lower()
                if account_type != 's' and account_type != 'c':
                    print("Please enter a valid account type")
                    
                else:
                    break
            
            # validate email format
            while True:
                account_email = input("Email Address: ")
                if not re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",account_email,re.IGNORECASE):
                    print("invalid format. Enter a valid email address")
                else:
                    break

            print("Please wait while account number is being generated...")
            time.sleep(2)

            opening_b = str(opening_balance)
            
            print('Account created successfully! Account Number: ' + account_number)
            
            with open('customer.txt', 'a') as customer:
                customer.write('Account Name: ' + account_name + ', ')
                customer.write('Opening Balance: ' + opening_b + ', ')
                customer.write('Account Type: ' + account_type + ', ')
                customer.write('Account Email: ' + account_email + ', ')
                customer.write('Account Number: ' + account_number + '\n')

            time.sleep(2)
            after_login()

        elif staff_action == '2':
            def verify_account():
                print("Please type in your Account Number")
                acc_num_typed = input("> ")

                # fetch acc details from c.txt, account_display
                with open('customer.txt', 'r') as account:
                    for line in account.readlines():
                        values = line.split(',')
                        if acc_num_typed in line:
                            print('Account found')
                            print(line)
                            time.sleep(2)
                            after_login()
                    else:
                        print("Incorrect Account Number. Please type '1' to try again or any button to go back to the "
                              "previous menu")  
                        menu = input("> ")
                        if menu == '1':
                            verify_account()
                        else:
                            after_login()

            verify_account()

        elif staff_action == '3':
            print("Have a nice day!\n")
            
            os.remove('session.txt')  # delete user session on log out

            time.sleep(2)

            # return user to login page
            banking_system()

        else:
            print("Please check the option and select again")
            after_login()

    selected()


banking_system()
