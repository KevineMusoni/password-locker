import getpass
def passwordRequest():
    field = getpass.getpass()
    password=field
    if field==password:
        return True
        return False
if passwordRequest():
    print("successfully logged in")
else:
    print("invalid credentials")
    

