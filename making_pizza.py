# Interactive program making a pizza

# for i in range(3):  if you want to repeat the below process 3 times
wish_to_continue = 'yes'  # we will start with default value, to begin While loop
while wish_to_continue.lower() == 'yes':
    print("$$$$$$$$ Welcome to the Pizza Restaurant!! $$$$$$$$$")
    print('You have choice of 3 toppings.')
    topping1 = input('Please enter your first choice of pizza topping: ') # accepts values as text
    topping2 = input('Please enter your second choice of pizza topping: ')
    topping3 = input('Please enter your third choice of pizza topping: ')
    print(f"you have entered: '{topping1}'")
    print(f"you have entered: '{topping2}'")
    print(f"you have entered: '{topping3}'")
    print("--------- we started making your pizza --------------")
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    # requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    requested_toppings = [topping1, topping2, topping3]

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings: # scans the available_toppings list for requested_topping
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")
    wish_to_continue = input('Do you wish to continue? enter yes/no: ')

print("******* we are done for this session, thank you *********")