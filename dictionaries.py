# dictionaries are defined with {}
from typing import SupportsRound


friend = {
    # they have keys/value pairs
    "name" : "Alan Turing",
    "cell" : "12345",
    "birthday": "june 23"
}

# empty dictionary 
nothing = {}

# values can be anything 
superhero = {
    "name" : "Tony Stark",
    "level" : 2323, 
    "avenger" : True,
    "gear": [
        "fast cars",
        "money",
        "iron mans suit"
    ],
    "vehicle": {
        "make": "audi",
        "model": ["R8", "A4"]
    }
}

# get values with key name
print(superhero['name'])

#get method also works, and can have a 'fallback' or default value
print(superhero.get('name', 'Unkown'))

#call dictionary, then item, (if more then specify which item)
print(superhero['name'])

#the key is how you call back an item
print(superhero['avenger'])

#this is to print specifically a list item inside a dictionary 
print(superhero['gear'][1])

#to print a dictionary inside a dictionary
print(superhero['vehicle']['make'])

#if a dictionary has multiple values 
print(superhero['model'][1])