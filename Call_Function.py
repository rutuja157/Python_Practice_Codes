##Call Function
def reverse(string):
  if(len(string) == 1):
    pass
  else:
    #print(len(string))
    reverse(string[1:len(string)])
  print(string[:1], end=' ')
  return ;

str1 = "AB"
str2 = "CD"
Joinstrs = str1 + str2
print (Joinstrs)
if (len(Joinstrs)) % 2 == 0:
    print ( reverse(Joinstrs) ,end=" ")
else:
    print("length is odd")