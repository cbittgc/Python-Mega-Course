###############################################################
#  This is v1 of the first application from the Udemy course  #
#  The Python Mega Course: Build 10 Real Worls Applications   #
#                                                             #
#  Caio Bittencourt ---> github.com/cbittgc                   #
###############################################################

import json
import difflib

def ValidateQuery(query, dictionary): # this function checks if the word entered, or slight variations of it, is in the dictionary
    if query in dictionary.keys():
        Translate(query,dictionary)

    elif query.title() in dictionary.keys():
        Translate(query.title(),dictionary)

    elif query.upper() in dictionary.keys():
        Translate(query.upper(),dictionary)

    elif len(difflib.get_close_matches(query,dictionary.keys(),n=1)) > 0:
            corrected = difflib.get_close_matches(query,dictionary.keys(),n=1)[0]
            flag = input(f"Did you mean {corrected} (y/n)? ")
            print()
            if flag == "y":
                Translate(corrected,dictionary)
            print()
    
    else:
        print("Invalid word!")

def Translate(word, dictionary): # this function formats the output
    if type(dictionary[word]) == list:
        for item in dictionary[word]:
            print(item)
    else:
        print(dictionary[word])

def EngDict(): # this function acts as the main program
    execFlag = True
    
    with open('data.json') as json_file:
        dictionary = json.load(json_file)
    
    while execFlag == True:
        query = input("Enter word: ").lower()
        if query == "/e":
            print("Thank you for using my program!")
            execFlag = False
        else:
            ValidateQuery(query,dictionary)
    
if __name__ == "__main__":
    print(f'Dictionary program by Caio Bittencourt for Udemy\'s Python Mega Course\nTo exit the program type in \'/e\'')
    EngDict()
