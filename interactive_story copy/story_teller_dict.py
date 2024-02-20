# import dependencies
import time
import textwrap
import threading
#from playsound import playsound

story_content = {
    "legendary_traveler": {
        "text": [
            "In the depths of space, you are hailed as a legendary traveler and warrior, commanding a highly advanced spaceship. "
            "During an expedition, disaster struck as your ship was sucked into a wormhole. You initiated cryosleep, hoping to survive. "
            "After drifting in space for some time you are awoken by your ships AI Spilo, you find your ship damaged but repairable. "
            "Trying to survive, Spilo helps you land on a nearby planet inhabited by elf-like beings, known as the kingdom of Aarondor. "
            "They help repair your ship, but a looming threat of Orcish invasion hangs over the kingdom. "
            "The rulers, grateful for your assistance, ask for your aid in combat, promising further assistance in fixing your ship once the threat is vanquished."
        ],
        "audio": "legendary_traveler.mp3",
        "choices": ["Accept the offer and help the kingdom", "Refuse and leave the planet"]
    },
    "help_elves_win": {
        "text": [
            "After the battle, hailed as a hero for your pivotal role in saving Aarondor from the orcish invasion, you are celebrated as a savior of the kingdom. "
            "Although you are rewarded with land, titles, and money, you are left stranded, as your ship was irreparably damaged in the war. "
            "Despite the warm welcome and gratitude from the inhabitants, you can't shake the nagging feeling that something is off and you fear you have been deceived."
        ],
        "audio": "help_elves_win.mp3"
    },
    "refuse_aid": {
        "text": [
            "You distrust the elf's motives and refuse to be a pawn. As you desperately try and escape, the elves seize your ship, "
            "imprison you, and erase you from their history."
        ],
        "audio": "refuse_aid.mp3"
    },
    "help_elves_lose": {
        "text": [
            "Despite your valiant efforts, the war against the orc invaders proves futile, ending in defeat for Aarondor's forces. "
            "Amidst the chaos of battle, you are captured by the victorious orcs and branded a war criminal for your role in resisting their conquest. "
            "Bound by chains and stripped of freedom, you are imprisoned within the dark confines of their stronghold, "
            "your hopes of redemption further obscured by the shadow of defeat. Yet, even in captivity, the flames of determination flicker within you, "
            "driving you to seek a path to redemption and liberation, even amidst the direst of circumstances."
        ],
        "audio": "help_elves_lose.mp3"
    },
    "life_in_aarondor": {
        "text": [
            "Unable to leave the planet, you integrate into Aarondor's society and the disheartening realization dawns upon you: "
            "you unknowingly fought for a corrupt regime reminiscent of the orc invaders. Motivated by a longing for redemption and justice, "
            "you embark on a quest to uncover ancient magic and relics rumored to offer a glimmer of hope amidst the prevailing despair. "
            "However, your relentless pursuit of truth and power does not escape the notice of the ruling elite, who perceive your actions as a threat to their authority. "
            "Yet, beneath the surface lies a deeper truth: an ancient curse has kept Aarondor locked in a state of perpetual war for millennia. "
            "Your quest for the elusive relics and magic becomes not only a means of redemption but also a potential key to breaking the curse, "
            "bringing an end to the cycle of strife that has plagued the land for so long. Betrayed by informants, you find yourself branded as a heretic and rebel. "
            "Ultimately you are apprehended and imprisoned."
        ],
        "audio": "life_in_aarondor.mp3"
    },
    "introduction": {
        "text": [
            "The once great Kingdom of Aarondor is now just a shadow of its former self. "
            "Torn apart by corruption and despair, the people have lost all hope that things will get better. "
            "You have been imprisoned for opposing the tyrannical rule that has engulfed the land for centuries. "
            "Your mistake was searching for lost relics that could lift the ancient curse and overthrow the ruling class; you have been imprisoned and forgotten. "
            "The months have turned into years with only the memories of a life once lived and the company of your thoughts echoing in the silence."
        ],
        "audio": "intro.mp3"
    },
    "cell_description": {
        "text": [
            "Every day is the same, you wake up in a cold dark prison cell. The cell is small, with walls of unyielding stone, and always damp. "
            "Between the darkness and the cold, with nothing but the floor for a bed, you think, 'If there is such thing as hell, I have found it.' "
            "Death would be a kindness. In the endless silence and darkness, the only light you have filters in through a tiny window high up on the wall. "
            "The door is solid metal and has seldom opened in the years you have been here. With only a small slot at eye level, you know very little of the world beyond."
        ],
        "audio": "cell.mp3"
    },
    "mysterious_visitor": {
        "text": [
            "As you ponder your life, or rather, what is left of it, you hear the slot on the door slide open. "
            "You peer out trying to focus in the darkness and are met with a strangely familiar pair of eyes. "
            "Although you can't quite place where you have seen these eyes before, the lines on his face tell a tale of a life fully lived. "
            "You can't help but think you must have met this stranger in a previous life. "
            "The stranger slips into the shadows as if to hide his identity and begins to speak softly. "
            "'There is a way out, you know, a way to change all of this,' he whispers. "
            "'A way to go back, back before the world we live in now and prevent 'this' future from ever happening.'"
        ],
        "audio": "visitor.mp3",
        "choices": ["Listen to the stranger", "Ignore the offer and stay in the cell"]
    },
    "listen_to_stranger": {
        "text": [
            "The stranger's voice becomes barely audible as if the walls are listening. 'It is said that long ago, Aarondor was a land of prosperity, "
            "ruled by wise kings and queens. It is believed that the curse that befalls Aarondor today was born from an ancient relic. "
            "This relic, shrouded in legend and whispers, was sought by a ruler only known in our history as the ancient king, a ruler whose ambition turned to madness. "
            "He believed the relic would grant him immortality, but its power was far more sinister, twisting the fate of the entire kingdom.' "
            "You listen intently as he continues, 'The key to saving Aarondor lies in its past. The events that led to its downfall, the rise of the Ancient King, "
            "the quest for the ancient relic, all pivotal moments that forged our cursed reality. "
            "Your mission, should you choose to accept it, is to journey back and unravel these events, alter their course that you might prevent the kingdom's fall. "
            "But beware, the past is a tapestry woven with the threads of countless lives. Changing it could unravel realities in ways we cannot predict.'"
        ],
        "audio": "listen.mp3"
    },
    "declining_choice": {
        "text": [
            "You decide to ignore the offer thinking it is meant to torture you into thinking there is a way out. Months blend into years, "
            "and your hope fades into the darkness of the cell. At last your suffering comes to end, right before you pass into oblivion you think "
            "'what might have been.'"
        ],
        "audio": "decline.mp3"
    },    
    "time_machine_explanation": {
        "text": [
            "Curiosity piqued, you move closer. The stranger removes a small intricate device unlike anything you've ever seen - "
            "a perfect fusion of ancient craftsmanship and futuristic technology. "
            "'This,' he begins, 'is not just a relic of the past, but a key to unlocking it. With this, you can change the past, altering the course of events that led us here. "
            "But there's a catch – if you go back, you can never return. As far as I can tell it's a one-way ticket,' he explains, "
            "his eyes locking with yours to emphasize the weight of his words. 'Your path forward will be in a reality you've rewritten.",

            "The device, resembling an armband, is adorned with symbols that glow faintly, it is covered in ancient runes and symbols you have never seen, "
            "it's both beautiful and terrifying all at once. The stranger continues, 'It's powered by a rare combination of magic and advanced technology, lost to us now. "
            "When activated, it will create a temporal rift, a doorway to a pivotal moment in our history. But once you step through, the rift will close forever, "
            "leaving no way back to the present. ",

            "The journey will be perilous, and the consequences of your actions unpredictable. "
            "History is a delicate tapestry, and altering its threads could unravel realities in ways beyond our understanding. "
            "This mission, should you choose to accept it, is a leap into the unknown, a gamble with time itself."
        ],
        "audio": "time_machine.mp3",
        "choices": ["Accept the one-way mission", "Refuse and stay in the present"]
    },
    "accept_mission": {
        "text": [
             "The stranger reaches out passing the relic through the slot in the door as it glimmers in the dim light. "
            "'This armband is a relic from a time when our kingdom balanced on the edge of magic and machine. "
            "Only the high rulers were allowed to wield such power while denying it to the people,' he explains. "
            "As you reach out, a distant noise of a guard's movement echoes through the corridor. The stranger's eyes widen with urgency. "
            "'There is more to tell, but we have no time. It is now or never.'",
            
            "Make your choice!"
        ],
        "audio": "accept_mission.mp3",
        "choices": ["Take the armband and accept the mission", "Refuse and stay in the present"]
    },
    "decline_mission": {
        "text": [
            "You decide to ignore the offer thinking it is meant to torture you into thinking there is a way out. Months blend into years, "
            "and your hope fades into the darkness of the cell. At last your suffering comes to end, right before you pass into oblivion you think "
            "'what might have been.'"
        ],
        "audio": "decline_mission.mp3"
    },        
    "end_of_chapter_one": {
        "text": [
            "The room begins to spin, the walls blurring into a vortex of time and space. The armband glows fiercely, pulsating with a life of its own. "
            "The runes etched into its surface ignite in a dance of arcane light, intertwining technology and magic in a cosmic symphony. "
            "A surge of ancient power pulses through you etching ancient symbols across your entire body, "
            "In a desperate attempt you firmly clasp the band around your wrist trying to remove it. Your heart races as time and space bend around you. "
            "The cold, dark cell dissolves into streams of light and dark that whisk you away from the present, hurtling you through the corridors of time. "
            "You, brace yourself for the unknown, the world around you is a whirlwind of light and echoes. You fear that this may be the end. Suddenly, everything stops. "
            "The light fades, and a heavy silence falls. You open your eyes to find yourself in a place long forgotten. "
            "Gone are the stone walls of your cell, replaced by a lush, vibrant forest. The sun is shining and the air is fresh with sounds of nature all around you. "
            "You think 'Aarondor has not seen the likes of this in a very long time.'",

            "As you take in your surroundings, a figure emerges from beyond the trees. "
            "Not a guard or a fellow prisoner, but a creature of legend long since extinct, and yet here it is. Standing before you is a Dragon, "
            "its scales shimmering with the hues of a thousand gems under the sunlight. Each scale is a masterpiece, reflecting light in dazzling patterns of gold, "
            "emerald, and sapphire. Its eyes, deep pools of ancient wisdom, fix upon you with an intensity that is both unnerving and majestic. "
            "A plume of smoke drifts from its nostrils, and its wings, vast and powerful, unfurl with a grace that belies their strength. "
            "The dragon's presence is overwhelming, yet there is a sense of intelligence and curiosity in its gaze that suggests it is more than just a wild beast. ",

            "As you stand frozen, the dragon tilts its head, considering you with an almost discerning look. "
            "The air around you seems to vibrate with an unspoken understanding between two beings, thrown together by the whims of fate. "
            "Yet, in this moment of awe, a chilling thought crosses your mind - you cannot tell if this magnificent creature plans to help you...or consume you.",
            
            "To be continued...",
            
            "End Chapter One."
        ],
        "audio": "chapter_end.mp3"
}
}

# Story Teller

class Story_Teller:
    def __init__(self, story_content):
        self.story_content = story_content
        self.speak_enabled = False

    def get_user_choice_speak(self):
        while True:
            choice = input("Would you like the story to be read aloud to you? (yes/no): ").strip().lower()
            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                return False
            else:
                print("Invalid choice. Please enter yes or no")

    def play_audio(self, file_path):
        try:
            playsound(file_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    def play_audio_once(self, audio_file):
        if self.speak_enabled:
            audio_thread = threading.Thread(target=self.play_audio, args=(audio_file,))
            audio_thread.start()
            return audio_thread
        return None

    def print_formatted_paragraphs(self, paragraphs, audio_file=None):
        # Play audio if enabled and file provided
        if self.speak_enabled and audio_file:
            audio_thread = threading.Thread(target=self.play_audio, args=(audio_file,))
            audio_thread.start()
        else:
            audio_thread = None

        # Print each paragraph with text wrapping
        for paragraph in paragraphs:
            wrapped_text = textwrap.fill(paragraph, width=100)
            self.slow_print(wrapped_text)
            print()  # Print a newline between paragraphs

        # Wait for audio to finish if it was started
        if audio_thread:
            audio_thread.join()

    def slow_print(self, text):
        for character in text:
            print(character, end='', flush=True)
            time.sleep(.0025) # .0625 is the best setting for a good reading speed
        print()

    def make_choice(self, prompt, options):
        while True:
            print("\n" + prompt)
            for number, option in enumerate(options, 1):
                print(f"{number}. {option}")
            choice = input("Enter your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return int(choice)
            else:
                print("Invalid choice. Please enter a valid number.")

    def start_chapter(self, chapter_name):
        self.speak_enabled = self.get_user_choice_speak()
        chapter_method = getattr(self.story_content, chapter_name, None)
        if callable(chapter_method):
            chapter_content = chapter_method()
            for content_method in chapter_content:
                result = self.process_story_part(content_method)
                if result is not None:  # Assuming choices return an integer or None
                    break  # or handle the choice result as needed
        else:
            print(f"Chapter '{chapter_name}' not found.")

    def process_story_part(self, story_part):
        text, audio_file, choices = story_part()  # Extract content from the story part
        self.print_formatted_paragraphs(text, audio_file)  # Display text and play audio

        if choices:
            prompt, options = choices
            decision = self.make_choice(prompt, options)
            next_part = None
            
            if decision == 1:
                next_part = self.story_content.next_part_after_accepting()  # Placeholder for actual method
            elif decision == 2:
                next_part = self.story_content.next_part_after_declining()  # Placeholder for actual method

            if next_part:
                self.process_story_part(next_part)  # Recursively process the next part of the story

# Main function

def main():
    print("Welcome to KRONUS GATE\n")
    
    story_teller = Story_Teller(story_content)


    story_teller.get_user_choice_speak()

    # Start the story from the beginning
    current_segment_key = "legendary_traveler"
    while current_segment_key:

        user_choice = story_teller.process_story_part(current_segment_key)

        if user_choice == "Accept the offer and help the kingdom":
            current_segment_key = "help_elves_win"   
        elif user_choice == "Refuse and leave the planet":
            current_segment_key = "refuse_aid"  
        elif user_choice == "Listen to the stranger":
            current_segment_key = "listen_to_stranger"   
        elif user_choice == "Ignore the offer and stay in the cell":
            current_segment_key = "declining_visitor_offer"  
        elif current_segment_key == "help_elves_win":  
            break
        elif current_segment_key == "refuse_aid":
            break  
        else:
            print("This part of the story has concluded.")
            break 

        if current_segment_key == "special_ending":
            print("You've reached a special ending. Congratulations!")
            break  

    print("Thank you for playing. I hope you enjoyed the story.")

if __name__ == "__main__":
    main()
