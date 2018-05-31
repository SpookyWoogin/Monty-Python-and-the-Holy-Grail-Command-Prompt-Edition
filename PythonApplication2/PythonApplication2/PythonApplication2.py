print("""Hello, and Welcome to Monty Python and the Holy Grail: Command Prompt Edition! Please start by entering your character 
data.""")


#Character Creation
username = input("Name: ")
if len(username) > 0:
    userchecking = input("Ok, so your name is " + username + ", right? Y or N ")
    if userchecking == "Y":
        usernameprefix = input("Ok! What prefix would you like to be attached to your name? ")
    elif userchecking == "N":
        username = input("Okay, what would you like for your username to be instead? ")
        print ("Okay, your new username will be " + username)
        usernameprefix = input("Ok! What prefix would you like to be attached to your name? ")
    else:
        print("Congrats. your name is now Code Mc Breaky, dick.")
        username = "Code"
        usernameprefix = "Mc Breaky"
else:
    print ("NO BREAKING MY CODE. ONLY I AM ALLOWED TO BRICK THE CODE.")
user = username + " " + usernameprefix
print("Ok! your final name shall be " + user)
input("Hit enter to progress into the story.")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

#Start of scenarios
print("Whilst traveling through a forest, " + user + """ and Patsy Discover two armourclad men fighting eachother, both with their
faces covered. As the fight ensues, one of the men, dressed in black armour defeats the other, killing him whil he does so. As
he is victorious he retreives his sword and stands tall. What do you do?""")
blacknight1 = input("Do you leave, or do you approach the armed man? ")
if blacknight1 == "approach":
    print("You chose to approach the man. As " + user + " approaches, he praises the man for his victory.")
elif blacknight1 == "leave":
    print("You chose to leave the forest, as to not anger the man and end up in the same situation as the man before you")
else:
    print("You chose to stare blankly at the man and not to anything. How curious?")