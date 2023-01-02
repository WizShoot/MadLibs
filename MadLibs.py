#intro
print("Hello!")
name = str(input("What is your name? "))
print("Hello,",name,"! This is a Mad Libs Program. Do Enjoy!")

#Loop
loop = 1
while (loop > 0):

#Taking input
    name2 = str(input("Enter a name for the story: "))
    adj = str(input("Enter an adjective: "))
    pnoun = str(input("Enter a plural noun: "))
    verb = str(input("Enter a verb in the first form of future tense: "))
    adverb = str(input("Enter an adverb: "))
    num = int(input("Enter a number: "))
    place = str(input("Enter the name of a place: "))
    gname = str(input("Enter the name of your favorite god: "))

#story
    print("--------- Mad Libs by WizShoot -----------")
    print("You should never mess with",name2,"for he may be friends with the",adj,pnoun,".")
    print("They may",adverb,verb,"you",num,"times in/on the face in",place,".")
    print("Anyways, worship",gname,"like you do and you'll be saved.")
