from user_1 import User, Credentials
def function():
	print(" __      __   ___ ____  __                      ")
	print("|  |    |  | |            |   \            /    |")
	print("|  |    |  | |            |    \          /     |")
	print("|  |    |  | |            |     \        /      |")
	print("|  |    |  | |__ ___ ___ _|      \      /       |")
	print("|  |____|  | |                    \    /        |")
	print("|          | |                     \  /         |") 
	print("|   ____   | |                      ||          |")
	print("|  |    |  | |                      ||          |")
	print("|  |    |  | |                      ||          |")
	print("|  |    |  | |                      ||          |")
	print("|__|    |__| |__ __ __ ___          ||          |")
	print("                                                0")
	
function()

def createUser(user_name, password):
  new_user = User(user_name,password)
  return new_user

def saveUserDetails(user):
  user.user_save()
def displayUsers():
   return User.display_users()

def loginUser(user_name,password):
  validation = Credentials.validation(user_name,password)
  return validation

def createCredential(account_name,account_username, account_password):
  newCredential = Credentials(account_name,account_username,account_password)
  return newCredential

def saveCredential(credential):
  credential.saveAccount()

def deleteAccount(credential):
  credential.deleteAccount()

def displayAccounts():
  return Credentials.displayAccounts()
  
def generatePassword():
  passwordGenerate = Credentials.generatePassword()
  return passwordGenerate

def main():
  print("Welcome to Password Locker!")
  while True:
    cmd_i_ = input("Type create to create a new user account, and q to quit")
    
if cmd_i == "q":
        print("Thank you for for using password locker! ")

elif cmd_i == "create":
        print("Sign Up")
        user_name = input("User_name: ")
        password = input("Password: ")
        saveUserDetails(create_user(user_name,password))
        print('\n')
        
        print(f"succesfully created...")
        
elif cmd_i == "show":
        if displayUsers():
            print("Below is the list of users:")
            print('\n')
            for user in displayusers():
                print(f"{user.user_name}")
                print('\n')
        else:
            print("data not found")
                
        
elif cmd_i == "login":
        print("Enter your User name and your Password to log in:")
        user_name = input("User name: ")
        password = input("password: ")
        log_in = login_user(user_name,password)
        if log_in == True:
            print("Welcome to Passsword Locker!")
            while True:
                cmd_i = input("Type create to create an account show to display the list of your accounts, q to quit \n")
                if cmd_i == "create":
                    print("Create new account")
                    account_name = input("Username: ")
                    account_username = input("Account Name: ")
                    password_option = input("choose: (existing password) or (new password) \n").strip()
                    while True:
                        if password_option == "existing password":
                            account_password = input("password: ")
                            break
                        elif password_option == "new password":
                            account_password = generatePassword()
                            break
                        else:
                            print("invalid input...")
                            break
                    save_credential(create_credential(account_name,account_username,account_password))
                    print({account_name}{account_username} {account_password})
    
                elif cmd_i == "show":
                    if displayAccounts():
                        print("List:")
                        for account in displayAccounts():
                            print({account.account_name}{account_username}{account_password})
                    else:
                        print("not found...")
                        
                elif cmd_i == "q":
                    print("Thank you for for using password locker! ")
                    break
                else:
                    print("Not a known command")
        else:
            print("Create an Account")

if __name__ == '__main__':
  main()