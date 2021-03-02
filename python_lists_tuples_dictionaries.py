#lists
shopping_list = ["cheese", "avocados", "apples"]
shopping_list.append("sugar")
shopping_list.remove("avocados")
#replace
shopping_list[0] = "skimmed milk"

print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])
print(len(shopping_list))
#for 1 and 2
print(shopping_list[:2:])
#for 1 and 3
print(shopping_list[::2])

#tuples (unchangable lists)
shopping_tup = ("Steak", "Tortellini", "Baguette")
print(shopping_tup)
print(type(shopping_tup))
print(shopping_tup[0])

#dictionaries
new_dict = {"my_key": "bees", "numberwang": 42,
"key_list": ["home", "backdoor", "garage"]}
new_dict["my_key"] = "hill"
print(new_dict)
print(new_dict["numberwang"])
print(new_dict["key_list"][1])
print(new_dict.keys())
print(new_dict.values())
