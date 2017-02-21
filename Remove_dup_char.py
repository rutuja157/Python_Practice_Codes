##Remove characters from the first string which are present in the second string
string1 = "aaaavvddddddvvddddddddjjjjjjjjgggggggggggg"
string2 = "avdzjjhhhh"


ListOfChar1 = list(string1)
ListOfChar2 = list(string2)
#chardict = dict()

for char in ListOfChar1:
  if char in ListOfChar2:
    del[char]
    #print ("character is present")

  else:
    print (char)