##Looping

magicians=['elice' , 'david' , 'carolina']

for magician in magicians:
    print(magician)
    print("**************** this is repeatable line***********")
print("**************** this is Not repeatable line***********")

nums = [3,5,1,8]
# print list of square of these numbers
squares = [] # MUTABLE : CAN BE CHANGE
coordinates = (10,30) # tuple:immutable : you cannot change
for i in nums:
    print("calculating the square:", i)
    # print(i**2)
    squares.append(i**2)

print(i) # out of scope , i variable does not exist here , since we started the not-indented line
print("input list:", nums)
print("Generated list:", squares)

kebabs = ['chicken' , 'shish', 'adana' , 'lamb']

for kebab in kebabs:
    print(f"i like {kebab} kebab, :)")

print("i love having kebabs for lunch from turkish restaurant.")






