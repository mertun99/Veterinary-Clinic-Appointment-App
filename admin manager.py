from cs50 import SQL
from app import check_password_hash, generate_password_hash
db = SQL("sqlite:///all.db")

def create_admin():
    username = input("Enter your username: ")
    hashed_password = generate_password_hash(input("Enter your password: "))
    db.execute("INSERT INTO admins(login,hash) VALUES (?,?);", username, hashed_password)


def delete_admin():
    login = input("Enter login of the admin you want to remove: ")
    confirmation = input("Are you sure? Type YES to confirm: ")
    if confirmation == "YES" or confirmation == "yes":
        db.execute("DELETE FROM admins WHERE login = ?;", login)
    else:
        print("Cancelled!")



def delete_all_admins():
    print("--> WARNING <-- \nTHIS WILL REMOVE ALL ADMINS FROM DATABASE!  You will have to create new ones.")
    confirmation = input("Are you sure? Type YES to confirm: ")
    if confirmation == "YES" or confirmation == "yes":
        db.execute("DELETE FROM admins;")
    else:
        print("Cancelled!")


answer = input("Type 1 to create an admin \nType 2 to remove an admin \nType 3 to remove all admins and clear the database \nInput: ")
if answer == "1":
    create_admin()
elif answer == "2":
    delete_admin()
elif answer == "3":
    delete_all_admins()
else:
    print("Invalid input!")
