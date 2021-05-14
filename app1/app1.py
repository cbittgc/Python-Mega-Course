import json

def EngDict():
    with open('data.json') as json_file:
        englishDictionary = json.load(json_file)
    query = input("Enter word: ")
    print(englishDictionary[query.lower()])

if __name__ == "__main__":
    EngDict() 
