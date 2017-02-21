#first consicative alphanumeric character 
#find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

import re
custinput = str(input())
alphanumchars = (re.findall(r"(\w)",custinput))
lengthcharlist = len(alphanumchars)
count = 1
flag = 0

for i in range(0,lengthcharlist):
    if i != (lengthcharlist-1):
      if alphanumchars[i+1] == alphanumchars[i]:
          print(alphanumchars[i])
          flag = 1
          break
      else :
          count =  count+1  
    else:
      pass
     
      
if flag == 0:
  print("-1")
      