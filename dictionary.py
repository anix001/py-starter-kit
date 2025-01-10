# dictionary = a collection of {key:value} pair, ordered and changeable, no duplicates
# one type of collection


capitals = { "USA": "Washington D.C",
            "China":"Beijing",
            "India":"New Delhi",
            "Nepal":"Kathmandu"}

print(capitals.get("Nepal"))

print(capitals.keys(), capitals.values())

print(capitals.items())

for key, value in capitals.items():
    print(f"{key}: {value}")