#String compresssion

string = "bbbddddddddbbccc"
print(string)
charlist = list(string)
lengthcharlist = len(charlist)
print("length of the string:",lengthcharlist)
#i=charlist[0]
count = 1
#i=0 
list1 = list()

for i in range(0,len(charlist)):
    if i != (len(charlist)-1):
      if charlist[i+1] != charlist[i]:
          #print(charlist[i],count)
          list1.append(charlist[i])
          list1.append(count)
          count = 1
    
      else :
          count =  count+1  
    else:
      #print(charlist[i],count)
      list1.append(charlist[i])
      list1.append(count)
      #print(count) 
      

#print("total charactors:",list1)
newlength = len(list1)
print(" new lenght of string is:", newlength)

if lengthcharlist > newlength:
  print("string can be compressed like:", list1)

