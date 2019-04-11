#!/usr/bin/env python3.6
import string,random,time
from locker import Credentials
from locker import User


#fuction that creates a new account for user
def new_account(id,user_name,password):
    new_user = Credentials(id,user_name,password)
    return new_user

#function tht saves the new account
def create_user(user):
    user.create_account()

#function that authorizes user account
def authenticate(username,passkey):
    return Credentials.auth_user(username,passkey)

#function that creates new data entries
def new_user(user_id,data_id,app_name,app_key):
    new_user = User(user_id,data_id,app_name,app_key)
    return new_user

#function that saves the new password created
def add_data(data):
    data.add_password()

#function that displays the user data
def display_data(data,number):
    return User.display_data(data,number)

#function that checks if user exists
def user_existing(data):
    return User.existing_data(data)

#the password generator
def password_generator(count):
    password_list=[]
    counter = 1
    while counter<=count:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase )
        password_list.append(gen_password)
        counter+=1
    return ''.join(password_list)

#function to copy password to clipboard
def copy_password(number,count):
    User.copy_password(number,count)
    
def main():
    '''
    The main function
    '''
    my_id=0

    entries = []

    print("\n")
    print("---------Welcome to your Password Locker-----------")
    print("-"*20)
    while True:
        #interface that creates new account
        print("Type:\n  cc to create new account\n  ln to log in\n  ex to exit")
        input_text = input().lower().strip()
        if input_text == "cc":
            print("You Will Now Create A New Account:"+"\n"+"-"*20 + " \n Enter Username:")
            my_username = input("New Username: ")
            print(" Enter password:")
            my_password = input("New Password: ")

            print("\n")
            create_user(new_account(my_id,my_username,my_password))
            my_id+=1
            print(f" {my_username} has been initiated .\nLogin to continue")
            entries.append(0)
            print("-"*20)
       
        #log in interface
        elif input_text == "ln".lower():
            print("Enter username and password to continue:")
            print("-"*30)
            my_login = input("Username: ")
            my_key = input("Password: ")
            get_result = authenticate(my_login,my_key)
            if get_result == 0:
                print("\n")
                print("Invalid username and/or password")
                print("-"*25)
            elif get_result!=0:
                
                #logged in user's interface
                print("\n")
                print(f"Hello {get_result.user_name}! What do you want to do?")
                while True:
                    print("Type:\n  ap - Add Password\n  vp - View Passwords\n  cp - copy password to clipboard\n  lo - Log Out")
                    get_input = input().lower()
                    
                    if get_input == "ap":   #password add interface
                        print("Add Application/Website name and password to store them in the locker:")
                        print("Enter App/Website:")
                        my_app = input()
                        
                        #optional password generation
                        print("do you want a new password generated for you? \n Type y for yes \n n to input your own..")
                        pass_input = input().lower
                        if pass_input == "y":
                            print("please specify length of pasword you want to generate")
                            password_length = int(input("Length of password: "))
                            my_webkey = password_generator(password_length)
                        if pass_input == "n":
                            my_webkey = input()
                        else:
                            print("password locker does not understand your input")
                        
                        my_auth = get_result.auth
                        add_data(new_user(my_auth,entries[my_auth],my_app,my_webkey))
                        entries[my_auth]=entries[my_auth]+1
                        print("\nWait...")
                        time.sleep(1.5)
                        print("\n")
                        print(f"***Your password for {my_app} is {my_webkey}***")
                        print("-"*45)
                    #interface to view passwords
                    elif get_input == "vp":
                        if user_existing(get_result.auth):
                            length = entries[get_result.auth]
                            print(f"You have {length} passwords:")
                            print("\n")
                            data_my=0
                            while data_my < length:
                                get_password = display_data(get_result.auth,data_my)
                                print(f"{data_my+1}. {get_password.website} ---- {get_password.web_key}")
                                data_my+=1
                            print("\nEnter a command to continue")
                            print("-"*20)
                        else:
                            print("\nYou have no data.\nType ad to generate some passwords")
                            print("-"*20)

                    elif get_input == "cp":
                        if user_existing(get_result.auth):
                            print("Enter the index of password you want to copy:")
                            get_index = int(input("Enter index: "))-1
                            if get_index >= entries[get_result.auth] or get_index<0:
                                print("\n")
                                print(f"{get_index+1} is invalid. Enter the correct index of password to copy")
                                print("Type vp to confirm the correct index of password to copy")
                                print("-"*30)
                            elif get_index < entries[get_result.auth]:
                                copy_password(get_result.auth,get_index)
                                print("\n")
                                print(f"Password {get_index+1} on the list has been copied, and is ready for pasting")
                                print("-"*30)
                        else:
                            print("\nYou have no data.\nType ad to add some passwords")
                            print("-"*20)

                    elif get_input == "lo":
                        print("\n")
                        print(f"Goodbye {get_result.user_name}!")
                        print("-"*30)
                        break
                    
                    else:
                        print("Invalid entry. Enter command again")
                        print("\n"+"-"*40)

        elif input_text == "ex":
            print("\n")
            print(f"Goodbye!!")
            print("-"*30)
            break

        else:
            print("Invalid entry. Enter command again")
            print("\n"+"-"*40)


if __name__ == '__main__':
    main()