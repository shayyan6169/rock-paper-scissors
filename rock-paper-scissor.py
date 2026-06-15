import random
# '''
# 1 for rock
# 2 for paper 
# 3 for sissors'''

computer    = random.choice([1, 2, 3])
youdict     = {"r": 1, "p": 2, "s": 3}
youstr      = input("Enter your choice : ")
if youstr not in youdict: exit("Wrong key! Please enter r, p, or s only.")
reversedict = { 1: "rock", 2: "paper", 3: "sissors"}
you         = youdict[youstr]

print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

# right now we have two variables [you] and [computer]

if ( computer==1   and you==1):
    print("draw")
    
elif ( computer==1 and you==2):
    print("you won ")

elif ( computer==1 and you==3):
    print("you lose")

elif ( computer==2 and you==1):
    print("you lose")

elif ( computer==2 and you==2):
    print("draw")

elif ( computer==2 and you==3):
    print("you won")

elif ( computer==3 and you==1):
    print("you won")

elif ( computer==3 and you==2):
    print("you lose")

elif ( computer==3 and you==3):
    print("draw")



