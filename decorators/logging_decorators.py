from functools import wraps

def logging_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@logging_activity
def brew_chai(type, milk_status = "No"):
    print(f"Brewing {type} Chai with {milk_status} Milk")

brew_chai("Masala Chai")

