import string,random
# import user.py

class User:
    field =input("Enter Username:\n")
    field = input("Enter Password:\n")
    detailList=field
    print(field)
  detailList = []
def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
@classmethod
def saveCredentials(self):
    User.detailList.append(self)
@classmethod
def displayUsers(cls):
    return cls.detailList


    class Credentials:
        credential_list =[]
def validation(cls,user_name,password):
    
    for user in User.detailList:
      if user.user_name == user_name and user.password == password:
        return True
      return False

  
def saveAccount(self):
    
    Credentials.credential_list.append(self)

def deleteAccount(self):
    
    Credentials.credential_list.remove(self)

@classmethod


def displayAccount(cls):
    
    return cls.credential_list
  
def generatePassword(num):
    password=''

    for x in range(num):
      y = random.randint(0,50)
      password += string.printable[x]

    return password
print (generatePassword)

    

