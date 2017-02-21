##Print all the duplicates in the input string
String = "aaaavvddddddvvddddddddjjjjjjjjggggggggggggbc"
ListOfChar = list(String)
chardict = dict()

for char in ListOfChar:
  if char in chardict:
    chardict[char] = chardict[char] + 1
    
  else:
    chardict[char] = 1
    
for key, value in chardict.items():
  if value > 1:
    print (key)