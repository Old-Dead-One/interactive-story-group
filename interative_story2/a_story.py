

Name = input("Enter your name to begin.: ")



def interactive_story():
     print(f""" Hello there captain {Name}.This is spilo your artificial ai built into your space suit. I need to inform you \
     After space Travelling for hundreds of years you crashland through an interdimensional wormhole.\
     We seem to have crashlanded in a unkown world that is inhabited by elf like creatures.Which we seem to be in a elf home\
     and the elves seem to have  healed your bones with a spell. I have analysed the surroundings and have calculated an escape route """)
     print()
     print(" thank elf: ")
     print(" escape:")


     decision = input(" Enter text     thank elf   or    escape: ")

     if decision == "thank elf":
        Thank_elf()
     elif decision == "escape":
        escape_window()
     else:
         print("Try typing your decision again ")
         

def escape_window():
    print(" After getting up quickly, you run full speed towards the window & burst through with no fear, you stick the landing and start running at full speed ahead towards the forest and escape ")         
    print(" Your personal ai spilo convinces you that its worth leaving so you leave the planet")
    print("The End")




def Thank_elf():
    print(" You thank the elf for the hospitality.\
     Then a sheriff elf comes in the room and starts asking you questions about where your from and\
     what it is that you are doing on their planet? The sheriff says that the elf governor has asked to speak with you ")
    print()

    decision = input(" Enter text   speak to governor or decline ")
   
    if decision == "speak to governor":
        accept()
    elif decision == "decline":
        jail()
    else:
        print("Try typing your decision again")

def governor():
    print("You are in the Governors office. He has been waiting to talk to you. You discuss what happened and how you arrived to the planet. The govenour then asks what you like to do next")
    print()
    print("repair ship")
    print("fight")

    decision = input("Enter text  ship   or    fight")

    if decision == "repair ship":
        repair_ship()
    elif decision == "fight":
        fight()

def repair_ship():
    print(" You inform the Governor that you would like to retrieve your ship")
    print("You are escorted to a secret base. You have the E.A.S.A or elf nasa. help you modify your ship for improvments for wormhole travelling. you leave the planet")
    print("The end. Tnx for playing")

def fight():
    print("The Governor informs you of the 1000 year war that has been going on between the elf Society and the orlock kingdom.\
           You join the battle and recieve the highest rank possible Chief General.")
    print("secret mission")
    print("retire")
    
    a = input(" Do you choose to go on a secret mission or retire :")
    if a == "secret mission ":
        secret_mission()
    elif a == "retire":
        retire()
    else:
        print("Try typing the decision again ")

def secret_mission():
    print("Elf spies find out that they can impose a magic spell to your nuclear bomb to penetrate the spell protecting the orlock kingdom.\
    You and elf team 8 fly over the orlock kingdom at night and nuke em")
    print(" You are recognized as a hero that ended the 1000 year war and went down in elf history as the greatest legend of all time who saved them. ")
    print("The end. Tnx for playing")

def retire():
    print("Your retirement is sweet and you spend the rest of your days in the elf society. The end. Tnx for playing")


def accept():
    print("The Governor is glad to speak to you and asks  ")
    print()
    print

    decision = input("  ")


def jail():
    print(" For declinning to speak to the governor you are sentenced and are at jail. There are a lot of other mythical creatures there too.\
          You have a cell mate and you get along just fine with him. Jail is bad but not as bad is it is in the movies.\
          you meet a bunch of other inmates. ")
    print("good ")
    print("prison break.  ")

    decision = input(" Type your decision    good   or   prison break")

    if decision == "good":
        good()
    elif decision == "prison break":
        prisonbreak()
    else:
        print("Try typing the decision again:")



def good():
    print("You end up serving the full 2 years of prison and with good behaviour they let you out early and are finally free ")
    print()
    print("You lived happily ever after") 
    print("The end. Tnx for playing")


def prisonbreak():
    print("thinking of a plan")
    print(" You plan with the other inmates and your cell mate to create a large fight diversion. everyone is fighitng and you are running for your life \
     You and your cell mate go to your suit find the ai and find the ship.")
    print(" After leaving the planet you and your cellmate have a change of heart and become the new gaurdians of the galaxy.")
    print("The end. Tnx for playing")





interactive_story()


# The end. Tnx for playing