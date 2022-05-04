def login(database, username, password):
    if username in database and password == database[username]:
        print("Welcome")
        return username
    elif username in database and password != database[username]:
        print("Wrong password")
        return ""
    elif username not in database:
        print("User not found.")
        return ""

def register(database, username, password):
    if username in database:
        print("Username already registered")
        return ""
    else:
        username = username.lower()
        database[username] = password
        return username
