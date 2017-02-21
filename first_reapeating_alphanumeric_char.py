# print first reapeating alphanumeric char and if reapeating char not present print -1

import re

custinput = str(input())
alphanumchars = (re.findall(r"(\w)",custinput))
flag= 0

print(alphanumchars)
chardict = dict()

for char in alphanumchars:
    if char in chardict:
      chardict[char] = chardict[char] + 1
      print(char)
      flag = 1
      break
    else:
      chardict[char] = 1
      
if flag == 0:
    print("-1")
      