#Display Menu wether check in or out

#Check in- Prompt user for room number and names of who's staying

#Check out- Delete people from the room and room number

#Display everyone who is staying at the hotel currently

# import json
# fileN = "hotel.json"

# #update Hotel to match Hotel.json
# with open(fileN, 'r') as handle:
#     data = json.load(handle)

hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson']
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance']
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheous']
    },
}
#Menu
print('''   
    Hello there!

  1. Checking In
  2. Checking Out
''')

user_choice = input('1 or 2: ')
# creating the two options of check in or out

#option #1
if user_choice == '1' : 
    #prompt for room # and who staying 
    print('''
    What room? & Who is staying?
''')
    room = input('Room: ')
    person = input('First guest: ')
    people = []
    #adds first person
    people.append(person)
    #continues to ask for more guest until it breaks
    while True:
        des = input('More guest? (y/n) ')
        if des == 'y':
            #adds the additional guest
            person2 = input('Name: ')
            people.append(person2)
        else : 
            break
    #gets the floor number
    floor = str(room)

    #(hotel dictionary)(floor[0] = the first index of floor)(room is the second key)(all this to update people into the key of room) 
    hotel[floor[0]][room] = people 
    print(people)
    print(hotel)

if user_choice == '2' : 
    #delete dictionary of the room and people 
    print(''' 
    What was your room number?
    ''')
    room = input('Room: ')
    room_floor = room[0]
    room = hotel[room_floor]
    print(room)
    # del hotel[room_floor][room]
    # print(hotel)
    # print('''
    # Thank you for staying!
    #     ''')
        

    

# #creating a json
# with open(fileN, 'w') as handle:
#     json.dump(hotel, handle)


