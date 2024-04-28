cars = ["maybach","audi","ferari","lambo","tesla"]
nums = [4,6,2,11,2,3,-55]

print("************ permanent sorting ************")

cars.sort() # sorting the original list
nums.sort() # sorting the original list in ascending order
print("Permanent sorted cars, asc:", cars)
print("Permanent sorted nums,asc:", nums)



cars1 = ["maybach","audi","ferari","lambo","tesla"]
nums2 = [4,6,2,11,2,3,-55]

cars1.sort(reverse=True) # sorting the original list
nums2.sort(reverse=True) # sorting the original list in ascending order
print("Permanent sorted cars1,desc:", cars1)
print("Permanent sorted nums1,desc:", nums2)

print("************ temporary sorting ************")

cars2 = ["maybach2","audi2","ferari2","lambo2","tesla2"]
sorted_cars2 = sorted(cars2) # returns to new copy of the list
print("original cars2:",cars2)
print("sorted copy of cars2",sorted_cars2)

print("number of element in the list :", len(cars1))
print("number of element in the list :", len(cars2))
print("number of element in the list :", len(nums2))

print("reversing the list without sorting")
print("original:, cars2")
print("reversed cars2,this is not sorted",cars2)

# H/W :3.8 9 10
## end of file: all lists and varialbes die here ,i.e removed from the memory after excisin complated
