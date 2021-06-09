import json
file_name = "t2.json"

with open(file_name, "r") as handle:
    data = json.load(handle)

todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

def print_todo():
    print('------- Todos -------')
    count=1
    for todo in todos:
        print(f'{count}: {todo}')
        count += 1 
    print('--------------------')

with open(file_name, "w") as handle:
    data = json.load(handle)

while True:
    print("""
Choose and option:

1. Print Todo
2. Add Todo
3. Remove Todo
0. Quit
        """)
    user_choice = input('')

    if user_choice == '1':
        # print current todos
        print_todo()

    elif user_choice == '2':
        #add a new item
        new_item = input('What do you want to add? ')
        todos.append(new_item)

    elif user_choice == '3': 
        #delete a todo 
        print_todo()
            #ask user which item to delete 
        delete_index = int(input('Which item would you like to delete? '))
        #delete item from list by user provided index
        del todos[delete_index -1]
        
    elif user_choice == '0':
        #exit program
        break
