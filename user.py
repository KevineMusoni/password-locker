def passwordRequest():
    field = input("Enter Password:\n")
    password=field
    print(field)
    if field==password:
        return True
        return False
if passwordRequest():
    print("successfully logged in")
else:
    print("invalid credentials")
    

