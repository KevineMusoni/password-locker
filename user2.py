# saving password in an external text file and changing password  
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
	print("Type c to change username and password, and q to quit")
	cmd = input("-> ")

	if cmd == "c":
		print("Fill in the form:")
		new_usr = input("New Username: ")
		newusr = open("username.txt", "w")
		newusr.write(new_usr)
		newusr.close()

		new_psw = input("New Password: ")
		newpsw = open("password.txt", "w")
		newpsw.write(new_psw)
		newpsw.close()

	if cmd == "q":
		sleep(1)
		running = False

        