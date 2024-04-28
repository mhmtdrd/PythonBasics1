student1 = {"name" : "john" , "city" : "brooklyn"}
student2={}

print("accessing the values:")
print(student1["name"])
print(student1["city"])

print("update or assign a new value, adding new key-value pair")
student1["city"] = "manhattan"
print("updated city:" , student1["city"].title())
student1["country"] = "USA"
print(student1)
student1["classes"] = ["sql" , "linux"]
print(student1)
print(student1["classes"][0])

print("removing the key- value pair from the dictionary")
del student1 ["country"]
print(student1)


print("********************************")
rivers = {"tuna" :"austria",
          "firat":"turkey",
          "volga" : "russia",
          "kongo" :"kongo",
          "mtkyari" : "georgia"}
for river, country in rivers.items():
    print(f"the {river.title()} runs through {country.title()}.")

print("************list of rivers we have in the list***********")
for river in rivers.keys():
    print(river.title())
print("************list of countries  we have in the list***********")
for country in rivers.values():
    print(country.title())








