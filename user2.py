# saving password in an external text file and changing password  
# use of if statements only no functions
from time import *
import random
import string

error = 0
running = True

username = open("username.txt", "r")
# look for the username.txt file and read from it
usernameRead = username.read()
username.close()

password = open("password.txt", "r")
# look for the password.txt file and read from it
passwordRead = password.read()
password.close()

user_name = input("Username: ")
if user_name == usernameRead:
	pass
else:
	error = 1

user_password = input("Password: ")
if user_password == passwordRead:
	pass
else:
	error = 1

if error == 1:
	print("error", random.randrange(0,50))
	sleep(1)
    # sleep() pauses the program.
	quit()
    #quit method exits a function/statement
else:
	pass

while running:
	print("Type c to change username and password And q to quit.")
	u_input = input()

	if u_input == "c":
		new_user = input("New Username: ")
		newuser = open("username.txt", "w")
		newuser.write(new_user)
		newuser.close()

		new_password = input("New Password: ")
		new_password = open("password.txt", "w")
		new_password.write(new_password)
		new_password.close()

	if u_input == "q":
		sleep(1)
		running = False


        