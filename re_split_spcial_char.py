# use of re.split with special characters

import re

n = str(input())
items = (re.split("[,\.]*",n))
#print (items)
for item in items:
    if item != "":
        print(item)
    else:
      pass