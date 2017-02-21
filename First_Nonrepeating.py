##First Non repeating Chracter

string = "rutujar"
charlist = list(string)

cdict = dict()

for char in charlist:
  if char in cdict:
    cdict[char] = cdict[char] + 1
    
  else:
    cdict[char] = 1

print (cdict)

for key, value in cdict.items():
  if value == 1:
    print (key)
    break