import datetime
from datetime import timedelta

from flask import redirect, render_template, session
from functools import wraps


def login_required(f): #from CS50
    """
    Decorate routes to require login.

    /
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/admin")
        return f(*args, **kwargs)

    return decorated_function



#https://www.programiz.com/python-programming/datetime
#https://www.geeksforgeeks.org/python-datetime-timedelta-function/
def get_time():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    max = datetime.datetime.now() + timedelta(days=90)
    max = max.strftime("%Y-%m-%d")
    current = datetime.datetime.now().strftime("%H:%M")
    print(today,max,current)
    return today,max,current

def apology(message, user):
    return render_template("apology.html", message = message, user=user)


def send_mail(message, user, date):
    print("\n")
    print("-------EMAIL--------")
    print("From: My Vet Clinic")
    print(f"To: {user['email']}")
    print(f"Subject: Your appointment request for {date['date']}")
    print(f"Message: {message}")
    print("-------EMAIL--------")
    print("\n")
