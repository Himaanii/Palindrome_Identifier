print("Enter a word")
a = []
r = []
word = input()
RevW = word[::-1]
l = len(word)
#print(l)
for i in range(l):
    a.append(word.upper()[i:i + 1])
    #print(a[i])
for i in range(l):
    r.append(RevW.upper()[i:i + 1])
    #print(r[i])
for i in range(l):
    if a[i] == r[i]:
        palindrome = True
        continue
    else:
        palindrome = False
        break
#print(palindrome)
if palindrome == True:
    print("Well done!", word, "is a palindrome.")
else:
    print("Sorry", word, "isn't a palindrome.")
