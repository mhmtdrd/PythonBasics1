for num in range(1,5): # generate number starting from 1, up to 5 ,incrementing by 1
    print(num)

print("****************range(10)***********")



for num in range(5,30,3):
    print(num,end="\t")


print("\n*****print odd numbers from 10 to 20*******")

for num in range(11,20,2):
    print("odd numbers:", end="\t")
    print(num , end="\t")


print("\n*****print squares of even numbers from 10 to 20*******")


print("even numbers:", end="\t")
squares = []
for num in range(10,21,2):
    print(num,end="\t")
    squares.append(num**2)
print("\nsquares of even numbers from 10 to 20:", squares)


print("************ find min and max from the given lst whitout usng min or max functions")

nums = [4,-22,2005,104,4]
nums.sort()
print(f"min:{nums[0]} and max:{nums[-1]}")



