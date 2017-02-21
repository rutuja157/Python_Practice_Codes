##Without using any string methods, try to print the following:without using string
## 123...N

def printo(i):
    count = 1
    
    while (count <= i):
        print (count,end="")
        count = count + 1
    #else:
     #   print("not valid")
        
    return;
    
print("enter no")
n = int(input())       
printo(n)