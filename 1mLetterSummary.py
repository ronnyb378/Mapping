#input a word 
#count every letter in the word 
#print how many times a letter repeates 

#blank dictionary for all letters 
so_far = {}

#create a function that splits the word into letters 
def lett(word):
    for letter in word:
        if letter in so_far:
            so_far[letter] += 1
        else:
            so_far[letter] = 1 
    print(so_far)

#enter a word 
word = input('Enter a word: ')

lett(word)

