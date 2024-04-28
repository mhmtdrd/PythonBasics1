# exercise 3.3
cars = ["masareti","maybach","mclaren"]

print(f"I would like to own a {cars[0].title()} car.")
print(f"I saw yesterday a {cars[1].title()} car.")
print(f"I used to have a {cars[2].title()} car.")
print(f"in italy a lot of  {cars[3].title()} car.")

print (f"{cars[-1].title()} is a supercar.")

print("**************** exercise 3.6 ********************")
guests.insert(0, "Brad Pitt")
guests.insert(3, "Leonardo di Caprio")
guests.append("Albert Einstein")

print(guests[1] + " can't make it.")
guests[1] = "Pink"
print(guests)

print(f"Hi {guests[0].title()}, please just come.")
print(f"Hi {guests[1].title()}, please just come.")
print(f"Hi {guests[2].title()}, please just come.")
print(f"Hi {guests[3].title()}, please just come.")
print(f"Hi {guests[4].title()}, please just come.")
print(f"Hi {guests[5].title()}, please just come.")
print(f"Hi {guests[-1].title()}, please just come.")


 nums = []
 for num in range(1,10000001):
     nums.append(num)
