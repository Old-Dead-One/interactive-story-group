import time 



class storyContent2:

    def __init__(self, name):
        self.name = name

    def space_crash(self):
        
        space_crash =                                                                            f"""Hello there captain {self.name}. This is Spilo, your artificial AI built into your space suit. I need to inform you After space traveling for hundreds of years you crashland through an interdimensional wormhole. We seem to have crashlanded in an unknown world that is inhabited by elf-like creatures. Which we seem to be in an elf home and the elves seem to have healed your bones with a spell. I have analyzed the surroundings and have calculated an escape route 
        """
        
        
        print(space_crash)
        print()
        while True:
            try:
                decision = input("Enter  thank elf   or   escape  : ").strip().lower()
                if decision == "thank elf":
                    self.thank_elf()
                    break
                elif decision == "escape":
                    self.escape_window()
                    break
                else:
                    raise ValueError("Invalid input. Please enter 'thank elf' or 'escape'.")
            except ValueError as ve:
                print(ve)

    def escape_window(self):
        escape_window = "After getting up quickly, you run full speed towards the window & burst through with no fear, you stick the landing and start running at full speed ahead towards the forest and escape.""Your personal AI Spilo convinces you that it's worth leaving so you leave the planet."
        
        print("You Leave and never look back.")
        print("The End")
        print(escape_window)

    def thank_elf(self):
        thank_elf =  """
        You thank the elf for the hospitality.
        Then a sheriff elf comes in the room and starts asking you questions about where you're from and 
        what it is that you are doing on their planet? The sheriff says that the elf governor has asked to speak with you."
         """ 
        print(thank_elf)
        
        while True:
            try:
                decision = input("Enter  speak to governor or decline : ").strip().lower()
                if decision == "speak to governor":
                    self.accept()
                    break
                elif decision == "decline governor":
                    self.decline_governor()
                    break
                else:
                    raise ValueError("Try typing your decision again.")
            except ValueError as ve:
                print(ve)
            

    def accept(self):
        print()
        accept_the_gov_req = [
            "The Governor is glad to speak to you and asks informs you of the planet's history and how they have been at war for centuries with the neighboring Orc planet. The governor asks for your help in defeating the Orcs. With your advanced technology, you can help them win the war. Inside your space ship there is a nuclear bomb that can destroy the Orc kingdom on the planet. The governor asks you to use it. What do you do?"
        ]
        print(accept_the_gov_req)


        print()
        while True:
            try:
                decision = input("Enter  fight Orcs  or decline fight  : ").strip().lower()
                if decision == "fight orcs":
                    self.fight_orcs()
                    break
                elif decision == "decline fight":
                    self.decline_fight()
                    break
                else:
                    raise ValueError("Try typing your decision again.")
            except ValueError as ve:
                print(ve)
    

    def decline_fight(self):
        decline_fight = "You decline to fight the Orcs. The governor has other plans for you. You are now treated as a traitor and sent straight to the dungeons of the elf jail."
        print(decline_fight)

    def fight_orcs(self):
        print()
        time.sleep(1)
        fight_orc = "As you affirm your commitment to the cause, anticipation crackles in the air like static before a storm. Elves, masters of ancient magic, converge upon your vessel, their arcane arts intertwining with the machinery of your ship. Through their enchantments, a shimmering shield of mystical energy forms, promising protection against the onslaught of plasma bullets that shall soon rain down upon you. With determination coursing through your veins, you step aboard your vessel, a lone sentinel amidst the vast expanse of space, poised to confront destiny head-on. The stage is set, the players assembled—brace yourself, for the dance of war awaits."
        print(fight_orc)
        time.sleep(5)
        print()
        print()
        betrayal = """Little did you know,  the governor harbors a dark secret—a clandestine plot to betray you despite your invaluable aid. With unwavering determination. The elf militaryads his forces into the galactic space battle, deploying the nuclear bomb entrusted to the marines stealth team. The devastating explosion anihalates the Orc kingdom, securing a decisive victory for the elves. Atlast victory smells so sweet.Yet, amidst the triumph, betrayal lurks in the shadows, waiting to strike with venomous intent. As the echoes of war fade into the distance. The entire time you were being used as a pawn in the governor's sinister game. He was always planning on sending you to prison after the war.You find yourself shackled, branded a traitor by the very one she sought to aid. The governor's deceitful machinations come to fruitionas you languish in a cell, betrayed and forsaken, your trust shattered like glass against the cold, unforgiving truth of betrayal."""
        print(betrayal)



    # So far i just need to create the function that will tie in the story to the actual asteroid game.
    # Also the decline option should go to jail to in alans story 
    def decline_governor(self):
        jail = "For declining to speak to the governor, you are sentenced and are at jail. There are a lot of other mythical creatures there too."
        "You have a cell mate and you get along just fine with him. Jail is bad but not as bad is it is in the movies."
        "You meet a bunch of other inmates."
        
        
        print(jail)
        print()
        while True:
            try:
         
                decision = input("Type your decision: serve good sentance or prison break: ")
                if decision == "serve a good sentance":
                    self.serving_a_good_sentance()
                    break
                elif decision == "prison break":
                    self.prisonbreak()
                    break
                else:
                    raise ValueError("Try typing the decision again.")
            except ValueError as ve:
                print(ve)

    def serving_a_good_sentance(self):
        alans_story = "This is a good area to implement Alan's story"
        print(alans_story)
      

    def prisonbreak(self):
        prison_break = " this is a good area to implement alans story"
        print(prison_break)
  

print()

name = input("Enter your name to begin: ")
story_instance = storyContent2(name)
story_instance.space_crash()
