import string

hesh = input("Write your new hashtag: ")

space = hesh.replace(" ", "")

for char in string.punctuation:
    space = space.replace(char, "")

words = hesh.split()
capitalized_words = [word.capitalize() for word in words if word]
result = "#" + "".join(capitalized_words)

if len(result) > 140:
    result = result[:140]

if len(result) == 0:
    print("Invalid hashtag")
else:
    print(result)
