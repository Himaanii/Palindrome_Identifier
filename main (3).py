print("Enter a word")
a = []
r = []
word = input()
l = len(word)

for character in word:
    a.append(character.lower())
    r.append(character.lower())

r.reverse()

#print(a)
#print(r)

if a == r:
    print("Well done!", word, "is a palindrome.")
else:
    print("Sorry,", word, "isn't a palindrome.")
