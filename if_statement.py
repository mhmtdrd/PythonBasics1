cars = ["masareti","maybach","mclaren",'bmw']

for car in cars:
    if car =='bmw' :
        print('this is the real beast' ,car.upper())
    else:
        print(car.title())

# == 'bmw' -> comparing the value ,expression returns true of false
#car = 'bmw' # assing the value to car variable

#expression that return true or false , can be use in the if statement
# true ,false
#3<5(false)
#num< 5 , num =10
#'tesla' in cars  - false /true
# car == 'bmw'

nums = [3,6,1,10,6]
#print " i got the number " whenever you fin number 6 in the list
# if you dont find number 6 then just print "next"

print('*************exercise****************')

for num in nums:
    if num != 6:
        print ("I got the number:" , num)
    else:
        print("next")

print("**************************** elif ************")

age = 15

if age <4:
        print('your ticket price (kids): , $4')
elif age < 16 :
    print("your ticket price (teens): $10")
elif age >65:
    print("your ticket price (senior): $12")
else: # else always in the end of if statement
    print("your ticket price (regular) : $15")

print("************** independent if statement ********")
if num < 8 :
    print('invalid entry ): ')

if age < 10:
    print("you can not go to scary movie") # what casese only this print no next
elif age < 18:
    print("you can not get driving licence") # only this tests : num ==> 11,17

# test scenorio:
#1. return firt statement only
#2, return second statement only
#3,return both statements
#4.return none of the statements

# test case :
#1. TS : n/A
#2.ts: num E( 11;17) - boundary testing
#3. ts : num E (........ ; 9 )
# , negative tc : num -1 --> requriment
#if min = 0 -- > negative tc : num = -1 --> requirement : eror : "invalid entry
#4.ts : num (18-180)





