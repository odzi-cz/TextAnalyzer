users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


def authenticate_user(username, password):
    if users.get(username) == password:
        return True
    else:
        print("Incorrect USERNAME or PASSWORD, please try again!")
        return False



