import time
print("""Hello, and Welcome to Monty Python and the Holy Grail: Command Prompt Edition! Please start by entering your character 
data.""")


#Character Creation
username = input("Name: ")
if str(username) == "debug":
    print ("Entered debugging mode. Name defaulted to Faggotoli the Great.")
    username = "Faggotoli"
    usernameprefix = "the Great"
    time.sleep(2)
elif len(username) > 0:
    userchecking = input("Ok, so your name is " + username + ", right? Y or N ")
    usercheck = str.lower(userchecking)
    if usercheck == "y":
        usernameprefix = input("Ok! What prefix would you like to be attached to your name? ")
    elif usercheck == "n":
        username = input("Okay, what would you like for your username to be instead? ")
        print ("Okay, your new username will be " + username)
        usernameprefix = input("Ok! What suffix would you like to be attached to your name? ")
    else:
        print("Congrats. your name is now Code Mc Breaky, dick.")
        username = "Code"
        usernameprefix = "Mc Breaky"
else:
    exit("NO BREAKING MY CODE. ONLY I AM ALLOWED TO BRICK THE CODE.")
user = username + " " + usernameprefix
print("Ok! your final name shall be " + user)
input("Hit enter to progress into the story.")

#Code Seperator

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
faces covered. As the fight ensues, one of the men, dressed in black armour defeats the other, killing him while he does so. As
he is victorious he retreives his sword and stands tall. What do you do?""")
time.sleep(7)
blacknight1 = input("Do you leave, or do you approach the armed man? ")
blackknight1 = str.lower(blacknight1)
if blackknight1 == "approach":
    print("You chose to approach the man. As " + user + " approaches, he praises the man for his victory.")
    time.sleep(1)
elif blackknight1 == "leave":
    print("You chose to leave the forest, as to not anger the man and end up in the same situation as the man before you")
    time.sleep(1)
elif blackknight1 == "hand him the communist manifesto":
    print("You have solved the worlds problems. Congradulations! Keep in mind, you didn't win, WE won.")
    time.sleep(5)
else:
    print("You chose to stare blankly at the man and not to anything. How curious?")
    time.sleep(5)
