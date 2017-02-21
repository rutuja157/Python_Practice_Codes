##write function

def reverse(string):
  if(len(string) == 1):
    pass
  else:
    #print(len(string))
    reverse(string[1:len(string)])
  print(string[:1])
  return;
  
reverse("GOD")