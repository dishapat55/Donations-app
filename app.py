from dis import show_code
from donation_pkg.homepage import show_donations, show_homepage, donate
from donation_pkg.user import login, register

global database
database = {"admin":"password123"}

global donations
donations = []

global authorized_user
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    make_choice = int(input("Choose an option: "))
    
    if make_choice == 1:
        username = (input("Enter your username: ").lower()) #(str(input('\nInsert name: ').lower().title()))
        password = (input("Enter your password: "))
        authorized_user = login(database, username, password)
        continue
    elif make_choice == 2:
        username = (input("Enter your username: ").lower())
        password = (input("Enter your password: "))
        authorized_user = register(database,username,password)
        if authorized_user != "":
            database[username] = password
            continue
    elif make_choice == 3:
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            continue
    elif make_choice == 4:
        show_donations(donations)
        continue
    elif make_choice == 5:
        print("Leaving DonateMe...")
        break