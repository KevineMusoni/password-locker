import random
import string
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
def save_credentials(self):
    User.detailList.append(self)
@classmethod
def display_users(cls):
    return cls.detailList


    class Credentials:
        credential_list =[]
# def check_user_exist(cls,user_name,password):
    
#     for user in User.detailList:
#       if user.user_name == user_name and user.password == password:
#         return True
#       return False

  
# def save_account(self):
    
#     Credentials.credential_list.append(self)

# def delete_account(self):
    
#     Credentials.credential_list.remove(self)

# @classmethod


# #   def generate_password


# def display_account(cls):
    
#     return cls.credential_list
  


