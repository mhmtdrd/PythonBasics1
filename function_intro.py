# Note : each function has a purpose , keep  it simple,it has a name,
# input/output,execution (call the function) , keep your functions simple

#name :lower case , should not start with number, use _ to sparate the words, give meaning ful names (summary)
#according to purpuse of the funtion
# defining the function / method
def greet_user():
    print("hello  user!")
    print("this function just for general greeting")

def greet_user_by_name(username):
    print(f"hello  {username.upper()}!")
    print("we want to greet any user by their name")

def add_numbers(num1,num2):
    print("----- this functions adds any given 2 numbers -------")
    print(f"addition of '{num1}' and '{num2}'")


#colling the method/function (execution)
greet_user()
greet_user()
greet_user_by_name("jhon")
greet_user_by_name("123")




friends= ['mehmet','palina','stela']
for friend in friends:
    greet_user_by_name(friend)



