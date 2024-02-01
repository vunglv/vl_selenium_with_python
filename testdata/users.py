users = [
    {"name": "Admin", "user_name": "Admin", "password": "admin123"}
]

def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)    