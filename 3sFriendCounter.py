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
    },
    {
        'name': 'Izak'
    },
    {
        'name:': 'Andy'
    }
    ],
    'friends_count': 0
}

#create function
def countFriends(dict):
    #checks length of 'friends' dictionary
    dict_length = len(dict['friends'])
    #sets the value to 'frinds_count'
    dict['friends_count'] = dict_length
    #prints how many friends
    print(dict_length)

#executes countFriends to ramit Dictionary 
countFriends(ramit)

