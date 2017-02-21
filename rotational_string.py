##A Program to check if strings are rotations of each other or not
string1 = "abcd"
string2 = "bcda"



combinestrings = string1 + string1
print (combinestrings)

len1 = len(string1)
len2 = len(string2)
result = "true"
#chardict = dict()
if len1 == len2:
    if string2 in combinestrings:
        print (result)
    
    else:
        result = "false"
        print(result)
else:
  print("strings are not rotations of each other")