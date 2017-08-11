import random

print ("hello, What is your fav No?")
no = input()
print "Your Favorite number is" , no 

minNo = 1
maxNo = 100
magicNo = random.randint(1,100)
 ##print ( magicNo )

message = "The magic number is between {0} and {1}"
print (message.format(minNo,maxNo))


found = False

while not found:
    print("Guess What it is")
    guess = input()
    
    if guess == magicNo:
        found = True
        print("***")    
    if guess < magicNo:
        print("Too Low")
    if guess > magicNo:
        print ("Too High")


##print("You Got it!")
