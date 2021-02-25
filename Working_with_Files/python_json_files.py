import json

new_dict = '{"name": "apple", "flavour":"tasty"}'

#create json file:
#with open("new_json_file.json", "w") as jsonfile:
    #json.dump(new_dict, jsonfile)
#load file:

# with open("new_json_file.json") as jsonfile:
#     fruit = json.load(jsonfile)
#     print(fruit['name'])
 #Failed attempt to add:
y = {"name": "banana", "flavour":"mushy"}
with open("new_json_file.json") as jsonfile:
    new_dict = json.load(jsonfile)
    y.update(new_dict)
print(json.dumps(new_dict))
#with open("new_json_file.json")








