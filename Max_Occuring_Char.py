##Max occuring chars
String = "aaaavvddddddvvddddddddjjjjjjjjgggggggggggg"
ListOfChar = list(String)
#print (ListOfChar)

CharInDictionary = dict()
 
for Char in ListOfChar:
    if Char in CharInDictionary:
      
      CharInDictionary[Char] =CharInDictionary[Char] + 1
      
    else:
      CharInDictionary[Char] = 1 
      
print(CharInDictionary)  
maxvalue = max(CharInDictionary, key=CharInDictionary.get)
print(maxvalue)

# by another method 

maxvalue = 0
maxChar = ''

for key, value in CharInDictionary.items():
  if value > maxvalue :
      maxvalue = value
      maxChar = key

print(maxChar +":"+str(maxvalue))
     