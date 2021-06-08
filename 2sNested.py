ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
    {
    'name': 'Jasmine',
    'email': 'jasmine@yahoo.com',
    'interests': ['photography', 'tennis']
    },
    {
    'name': 'Jan',
    'email': 'jan@hotmail.com',
    'interests': ['movies', 'tv']
    }
    ]
}

#get email address for Ramit
print(ramit['email'])

#get the first interest of Ramit
print(ramit['interests'][0])

#get email address of Jasmine
print(ramit['friends'][0]['email'])

#get second interest of Jan's
print(ramit['friends'][1]['interests'][1])