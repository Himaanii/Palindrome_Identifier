print("Enter a 3 letter word.")
a =[]
word = input()
a.append (word [:1])  
a.append (word [1:2])
a.append (word [2:3])
print(a[0])
print(a[1])
print(a[2])
if a[2] == a[0] and a[1] == a[1] and a[0] == a[2]:
  print("Well done!", word, "is a pallindrome.")
else:
  print("Sorry", word, "isn't a pallindrome.")