#define functions as steps to login


def enter_username(username):
    print("******* login page **********")
    print(f"you entered{username}")

def enter_password():
    pword=input('enter your password:')
    print(f"you entered ******{pword[-2:]}")

def click_login():
    print("login was clicked")
    print("you successfully logged in.")

def logout():
    print("you ssuccessfully logged out!")



