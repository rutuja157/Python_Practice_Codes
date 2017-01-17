##World Count 
String = "My Name is Rutuja my name is swapnil"
ListOfword = String.split()
print (ListOfword)
print ( len(ListOfword ))

WordInDictionary = dict()
 
for word in ListOfword:
    if word in WordInDictionary:
      WordInDictionary[word] = WordInDictionary[word] + 1
    else:
      WordInDictionary[word] = 1 
      
print(WordInDictionary)