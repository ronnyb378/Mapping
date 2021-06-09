import json
file_name = "super.json"

with open(file_name, "r") as handle:
    data = json.load(handle)

superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    },
    "style": "clean"
}

with open(file_name, "w") as handle:
    json.dump(superhero, handle)



#file_name is the variable for the file
#r is read vs w is write 
#handle is the variable that is set for this function
#json is the way we load and save, in this instence we read
with open(file_name, "r") as handle:
    data = json.load(handle)
    print(data)