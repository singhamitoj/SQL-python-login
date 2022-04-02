# SQL Universal Login System, by singhamitoj AKA GamerSinghKing.
# Created in a garage far, far away.
# This is the login code used in the SQL Multiplication Tester.
import sqlite3
import platform
import getpass
cos = platform.system()
user = getpass.getuser()
print("Welcome, " + user + "!")

def login(username, usrpass):
    try:
        data = sqlite3.connect("accounts.db")
        crsr = data.cursor()
        crsr.execute("SELECT * FROM users WHERE uid=? AND pass=?",(username,usrpass))
        if crsr.fetchone():
          #  print("Allow Login")
            return (True)
        else:
           # print("Disallow Login")
            return (False)
    except:
        print("Sorry, that user does not exist.")
        return(False)
    finally:
        data.commit()
        data.close()
uip_usrname = input("Username: ")
uip_usrpass = input("Password: ")
if login(uip_usrname, uip_usrpass) == True:
    print("Wow, it works!")
else:
    print("Wow, I never really needed this!")
    exit(1)
