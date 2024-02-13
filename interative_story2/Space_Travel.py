class storyContent2:

    def __init__(self, name):
        self.name = name

    def interactive_story(self):
        print(f""" Hello there captain {self.name}. This is Spilo, your artificial AI built into your space suit. I need to inform you \
        After space traveling for hundreds of years you crashland through an interdimensional wormhole. \
        We seem to have crashlanded in an unknown world that is inhabited by elf-like creatures. \
        Which we seem to be in an elf home and the elves seem to have healed your bones with a spell. \
        I have analyzed the surroundings and have calculated an escape route """)
        print()
        print("Thank elf:")
        print("Escape:")

        decision = input("Enter text: 'thank elf' or 'escape': ")

        if decision == "thank elf":
            self.Thank_elf()
        elif decision == "escape":
            self.escape_window()
        else:
            print("Try typing your decision again.")

    def escape_window(self):
        print("After getting up quickly, you run full speed towards the window & burst through with no fear, you stick the landing and start running at full speed ahead towards the forest and escape.")
        print("Your personal AI Spilo convinces you that it's worth leaving so you leave the planet.")
        print("The End")

    def Thank_elf(self):
        print("You thank the elf for the hospitality.")
        print("Then a sheriff elf comes in the room and starts asking you questions about where you're from and")
        print("what it is that you are doing on their planet? The sheriff says that the elf governor has asked to speak with you.")
        print()

        decision = input("Enter text: 'speak to governor' or 'decline': ")
    
        if decision == "speak to governor":
            self.accept()
        elif decision == "decline":
            self.jail()
        else:
            print("Try typing your decision again.")

    def accept(self):
        print("The Governor is glad to speak to you and asks...")  # Add your logic here

    def jail(self):
        print("For declining to speak to the governor, you are sentenced and are at jail. There are a lot of other mythical creatures there too.")
        print("You have a cell mate and you get along just fine with him. Jail is bad but not as bad is it is in the movies.")
        print("You meet a bunch of other inmates.")
        print("Good.")
        print("Prison break.")

        decision = input("Type your decision: 'good' or 'prison break': ")

        if decision == "good":
            self.good()
        elif decision == "prison break":
            self.prisonbreak()
        else:
            print("Try typing the decision again.")

    def good(self):
        print("You end up serving the full 2 years of prison and with good behavior they let you out early and you are finally free.")
        print()
        print("You lived happily ever after.") 
        print("The end. Thanks for playing.")

    def prisonbreak(self):
        print("Thinking of a plan...")
        print("You plan with the other inmates and your cell mate to create a large fight diversion. Everyone is fighting and you are running for your life.")
        print("You and your cell mate go to your suit find the AI and find the ship.")
        print("After leaving the planet you and your cellmate have a change of heart and become the new guardians of the galaxy.")
        print("The end. Thanks for playing.")



name = input("Enter your name to begin: ")
story_instance = storyContent2(name)
story_instance.interactive_story()
