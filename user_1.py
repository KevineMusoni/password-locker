import random
import string
from time import *
# user class

class User:

  userList = []
  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
  
  def saveUser(self):
    User.userList.append(self)

  @classmethod
  def displayAllUsers(cls):
    return cls.userList

# credentials class
class Credentials:
  credentialList =[]
  def __init__(self, account_name, account_username, account_password):
    self. account_name = account_name
    self.account_username = account_username
    self.account_password = account_password

  @classmethod
  def validation(cls,user_name,password):
    for user in User.userList:
      if user.user_name == user_name and user.password == password:
        return True
      return False

  
  def save(self):
    Credentials.credentialList.append(self)

  def delete(self):
    Credentials.credentialList.remove(self)

  @classmethod
  def displayAllAccounts(cls):
    return cls.credentialList
  def generatePassword():
    gen_pass = "".join(random.choice(char) for _ in range(10))
    return gen_pass
#   def generatePassword(num):
#     password=''

#     for x in range(num):
#       y = random.randint(0,50)
#       password += string.printable[x]
#       #string.printable[] is a combination of digits, ascii_letters, punctuation, and whitespace for password input.
#     return password
# print (generatePassword)