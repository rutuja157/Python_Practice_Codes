# consecutive repetitions in the string

string = "bbbddddddddbbccc"
charlist = list(string)
lengthcharlist = len(charlist)
print(lengthcharlist)
#i=charlist[0]
count = 1
#i=0 

for i in range(0,len(charlist)):
    if i != (len(charlist)-1):
      if charlist[i+1] != charlist[i]:
          print(charlist[i])
          print(count)
          count = 1
    
      else :
          count =  count+1  
    else:
      print(charlist[i])
      print(count) 