import json

data = json.load(open("data.json"))

def translate(w):
  w = w.lower()
  if w in data:
    return data[w]
  else:
    return "The word doesn't exist. Please try again."

word = input("Enter word:")

print(translate(word))

