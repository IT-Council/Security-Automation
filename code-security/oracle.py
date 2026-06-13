def is_admin(username):

    if username == "chowdary":

     return True 

    else:
    
     return False

print(is_admin("chowdary"))
print(is_admin("john"))
print(is_admin("admin"))


def check_user(username):
  
    if username == "admin":
       return "Welcome, admin!"
    
    else:
       return "Access denied. You are not admin."
    
    print(check_user("admin"))
    print(check_user("john"))   