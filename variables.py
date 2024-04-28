## comment line
# variables storage with reference , so we can use the value with reference
#variable name and file names
#lower_case,no_spaces(new_message),dont start with number
#SQL , java : CustomerID (sql) , newMessage(java)
msg = ('hello python')
message = " wow i am coding"
num = 123
a = 34
b = 88
status = True # boolean
print(a + b)
print(message)
print(msg , message)
print('*********reassigning the value for the variable**********')
print('old value:',msg)
msg = 'good morning'
print('new value:',msg)

x = 45
y = 55
print('1.sum of x and y:', x + y)
x = 145 # we reset the value to 145
print('2. sum of x and y:', x +y)

print('**************working with numbers****************')
num1 = 5
num2 = 3
print("result" , 5**3) #exponent : 5*5*5
print("modulo:" , num1 % num2)    #remainder 5 = 3+1 + 2 | x = a*b+ c
#when you divide number 'a' , floor division  returns a'b' --> 5 = 3+1 +2 | x = a*b + c(c<a)
print("floor division:" , num1 // num2)

# Odd numbers : 1 ,3 ,5 , ..... (not even number)
# even numbers : 2 , 4 ,6 ... (dividable by 2)

print("************useful functions while working with numbers****************")
print("regular division :" , 100/3)
print("int(100/3)")
print(float(100/2))

print ("************* useful function while working with mix data types *********")

age = 25
msg4 = "I am " + str(age + 2) + " years old" # converting int to a string with str () funtion
print(msg4)

msg4 = f" I  am {age} years old."

print(25+30) # 55 , we are adding numbers , calculation
print('25' + '30') # 2530 , wwe are just combining text , cancatenation









