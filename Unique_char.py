##Is Unique characters in string
String = "rutuja"
ListOfChar = list(String)
print (ListOfChar)

CharInDictionary = dict()
 
result = "true"

for Char in ListOfChar:
    if Char in CharInDictionary:
      result= "false"
      break
    else:
      CharInDictionary[Char] = 1 
     
print(result)  