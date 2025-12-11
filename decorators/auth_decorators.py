from functools import wraps

def authorization(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied! Only For Admins")
        else:
            return func(user_role)
    return wrapper

@authorization
def authorize_tea_inventory(role):
    print("Tea Inventory Authorized")

authorize_tea_inventory("user")
authorize_tea_inventory("admin")

