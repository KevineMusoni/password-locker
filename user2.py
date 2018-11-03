# saving password in an external text file and changing password  
# use of if statements only no functions
from time import *
import random
import string

error = 0
running = True

username = open("username.txt", "r")
usernameRead = username.read()
username.close()

password = open("password.txt", "r")
passwordRead = password.read()
password.close()

usr_user = input("Username: ")
if usr_user == usernameRead:
	pass
else:
	error = 1

usr_pass = input("Password: ")
if usr_pass == passwordRead:
	pass
else:
	error = 1

if error == 1:
	print("error", random.randrange(0,50))
	sleep(1)
    # sleep() pauses the program.
	quit()
else:
	pass

while running:
	print("Type c to change username and password And q to quit.")
	input = input()

	if cmd == "c":
		print("Fill in the following.")
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

        