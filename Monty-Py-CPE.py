import time
import sys
print("""Hello, and Welcome to Monty Python and the Holy Grail: Command Prompt Edition! Please start by entering your character 
data.""")


#Character Creation
username = input("Name: ")
if str(username) == "debug":
    print ("Entered debugging mode. Name defaulted to Devioli the All-Knowing.")
    username = "Devioli"
    usernameprefix = "the All-Knowing"
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
    print("""Invalid Name
        Reason:
           Name can't be blank.""")
    time.sleep(5)
    exit()
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

print("""Little is seen over a grassland besides fog, and the sound of a galloping horse in the backround. However, this sound is 
not a sound made on grass, but instead a sound made on cobblestone. From the fog emerge 2 pedestrians, """ + user + """, dressed in
 full chainmail and equipped with a crown on his head, and then there's Patsy, who's using two half coconuts percussively to make
  it sound like there is a horse on the path.""")
time.sleep(5)

#Castle Wall
print("""As you and Patsy travel along the trail, you come across a castle and Patsy manages to perfectly mimic the sound of a horse
 coming to a stop. Two guards then become barely visible atop the castle wall.""")
time.sleep(3)
castleencounter1 = input("""What do you choose to do? Do you choose to state your mission to the guards, or do you ask them who
 they are?: """)
castlecapfix1 = str.lower(castleencounter1)
if castlecapfix1 == "state your mission":
    print(user + """: Hello fine guards. I'm looking to recruit knights to join me at Camelot, and I'm also hoping to recruit the
     master of the castle.""")
    time.sleep(3)
    print("*The two guards seem to be distracted by the two half coconuts that Patsy has*")
    time.sleep(3)
    print("*How'd they get here? Did a bird perhaps carry it all the way to Mercia from the tropics?*")
    time.sleep(3)
    print("By now you and Patsy have become frustrated with the two guards, and you decide to leave.")
elif castlecapfix1 == "ask them who they are":
    print(user + ": Hello? Who goes there! I request to know who you are, as I am the honorable " + user + " of England.")
    time.sleep(4)
    print("*The two guards seem to be distracted by the two half coconuts that Patsy has*")
    time.sleep(4)
    print("*How'd they get here? Did a bird perhaps carry a whole coconut all the way to Mercia from the tropics?*")
    time.sleep(4)
    print("By now you and Patsy have become frustrated with the two guards, and you decide to leave.")
else:
    print("What did I tell you about breaking my code?")

#Black Knight [WIP]
print("Whilst traveling through a forest, " + user + """ and Patsy Discover two armourclad men fighting eachother, both with their
faces covered. As the fight ensues, one of the men, dressed in black armour defeats the other, killing him while he does so. As
he is victorious he retreives his sword and stands tall. What do you do?""")
time.sleep(7)
blacknight1 = input("Do you leave, or do you approach the armed man? ")
blackknight1 = str.lower(blacknight1)
if blackknight1 == "approach":
    print(user + ": ")
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
