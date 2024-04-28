#H/W build if logic
#print("fizz") when number is diviadble by 3,
#print("buzz") when number is diviadable by 5 ,
#print("fizzBuzz") when number is diviadble by 15,

for i in range(4) :
    num_str = input ("enter the number")
    num = int(num_str)
    if num <= 0:
       print("invalid entry")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
       print("buzz")
    elif num % 15 == 0:
       print("fizzbuzz")
    else:
       print("not dividable")

print("********************************************")


# H/W: build if logic:
# print("Fizz") when number is dividable by 3,
# print("Buzz") when number is dividable by 5,
# print("FizzBuzz") when number is dividable by 15
# Questions to Business:
# input should be more than zero, for 0 program should return "invalid entry"

for i in range(4):
    num = None
    num_str = input('enter the number:').strip()  # input returns a string data type
    if num_str == '':
        num = -1
    else:
        num = int(num_str)  # convert to num

    if num <= 0:
        print('invalid entry')
    elif num % 15 == 0:  # bug , report in JIRA
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print('not dividable')
# is returning error, which I don't understand, when I pass 'a' as input
# test cases, test data: 3, 5, any number dividable by 15, 17, string, 0, 34.55, ####, '   ', '\n'







