animal_type = input().lower()
result = "unknown"

if animal_type == "dog":
    result = "mammal"
elif animal_type == "crocodile" or animal_type == "tortoise" or animal_type == "snake":
    result = "reptile"


print(result)