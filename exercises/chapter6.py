print("****** exercise 6.11 ***********")
cities = {
    'New York': {
        'population': '9 mln',
        'country': 'USA',
        'fact': 'Big Apple'
    },
    'London': {
        'population': '6mln',
        'country': 'UK',
        'fact': 'rainy'
    },
    'Dubai': {
        'population': '3.4 mln',
        'country': 'UAE',
        'fact': 'expensive'
    },
    'Rome': {
        'population': '3 mln',
        'country': 'Italy',
        'fact': 'historical'
    }
}

# print(f"New York has 9 mln population and located in the USA, fun fact about: 'Big Apple'")

print(f"{list(cities.keys())[0]} has {cities['New York']['population']} population and located in {cities['New York']['country']}, fun fact about: '{cities['New York']['fact']}'")

print(f"{list(cities.keys())[0]} has {cities['London']['population']} population and located in {cities['London']['country']}, fun fact about: '{cities['London']['fact']}'")

print(f"{list(cities.keys())[0]} has {cities['Dubai']['population']} population and located in {cities['Dubai']['country']}, fun fact about: '{cities['Dubai']['fact']}'")

print(f"{list(cities.keys())[0]} has {cities['Rome']['population']} population and located in {cities['Rome']['country']}, fun fact about: '{cities['Rome']['fact']}'")

print("----- access with looping ------------")
for city, info in cities.items():
    print(f"{city.title()} has {info['population']} population and located in {info['country'].upper()}, fun fact about: '{info['fact']}'")


    print("********* additional on inpu *********")










