# using nested for loop and if statement

#if expression:
#    code to execute when expression1 returns true
#elif expression2:
 #   code to execute in case expression1 returns false and expression2 returns true
#elif ..
 #   ...
#else :
#code to excute when all aboce expressions return false
#nested for loop : loop inside loop

meals = ["hamburger","kebab","pizza",'plav']
drinks = ['water','milk','coffee','tea']
print('********* here is the all possible combination of meals and drinks*********')
for meal in meals:
    for drink in drinks:
        print(f"customer's order : {meal} and {drink}")

print("************* multiplication table ***********")

for i in range (1,11):
    for j in range(1,11):
        #"5*3 = 15"
        print(f"{i} * {j} = {i*j}" , end ="\t\t")
    print() # adds newline , hits enter with evey "f"

print("***********************")



print("************************ additional on input****" )

age_text = (input("enter your age"))
if age > 10:
    if age <20:
        print("more than 10 but less than 20")
    else:
        print("more than 20")
else :
    print("less or equal to 10")








