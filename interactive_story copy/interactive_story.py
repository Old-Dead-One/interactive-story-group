#
# import dependencies
#
import time
import textwrap
import threading
from playsound import playsound
#from gtts import gTTS
import os
#
# Utility functions:
# 

def play_audio(file_path):
    try:
        playsound(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
    
def play_audio_once(audio_file, speak_enabled):
    if speak_enabled:
        audio_thread = threading.Thread(target=play_audio, args=(audio_file,))
        audio_thread.start()
        return audio_thread
    return None

def print_formatted_paragraphs(paragraphs, speak_enabled, audio_file):      ### Formats printed text
    audio_thread = play_audio_once(audio_file, speak_enabled)
    
    for paragraph in paragraphs:
        wrapped_text = textwrap.fill(paragraph, width=100)
        slow_print(wrapped_text)
        print()
    
    if audio_thread:
        audio_thread.join()

def slow_print(text):                                           ### Slow the speed at which the text prints to the screen
    for character in text:
        print(character, end='', flush=True)
        time.sleep(.0625) # Print speed
    print()        

def get_user_choice_speak():                                    ### Allows user to choose wether the story is read out loud.
    while True:
        choice = input("Would you like the story to be read aloud to you? (yes/no): ").strip().lower()
        print()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid choice. Please enter yes | no ")
    
def make_choice(prompt, options):                              ### Utility "Make Choice" function
    while True:
        print("\n" + prompt)
        for number, option in enumerate(options, 1):
            print(f"{number}. {option}")
        choice = input("Enter your choice: ")
        print()
        if choice and choice in [str(num) for num in range(1, len(options) + 1)]:
            return choice
        else:
            print("Invalid choice. Please enter a valid number.")
#
# Story Content
#  
def introduction(speak_enabled):                                ### Introduction
    intro_text = [       
        "The once great Kingdom of Aarondor is now just a shadow of its former self. "
        "Torn apart by corruption and despair the people have lost all hope that things will get better. "
        "You have been imprisoned for opposing the tyrannical rule that has engulfed the land for centuries. "
        "Your mistake was searching for lost relics that could lift the ancient curse and overthrow the ruling class, you have been imprisoned and forgotten. "
        "The months have turned into years with only the memories of a life once lived and the company of your thoughts echoing in the silence."
    ]
    intro_audio = "intro.mp3"
    print_formatted_paragraphs(intro_text, speak_enabled, intro_audio)

    input("\nPress Enter to continue...\n")

def cell_description(speak_enabled):                            ### Prison cell description
    cell_text = [
        "Every day is the same, you wake up in a cold dark prison cell. The cell is small, with walls of unyielding stone, and always damp. "
        "Between the darkness and the cold, with nothing but the floor for a bed, you think, 'If there is such thing as hell, I have found it.' "
        "Death would be a kindness. In the endless silence, and darkness, the only light you have filters in through a tiny window high up on the wall. "
        "The door is solid metal and has seldom opened in the years you have been here. With only a small slot at eye level, you know very little of the world beyond."
    ]
    cell_audio = "cell.mp3"
    print_formatted_paragraphs(cell_text, speak_enabled, cell_audio)

def mysterious_visitor(speak_enabled):                          ### Mysterious Visitor 1st encounter
    visitor_text = [
        "As you ponder your life or rather, what is left of it, you hear the slot on the door slide open. "
        "You peer out trying to focus in the darkness and are met with a strangely familiar pair of eyes. "
        "Although you can't quite place where you have seen these eyes before the lines on his face tell a tale of a life fully lived. "
        "You can't help but think you must have met this stranger in a previous life. "
        "The stranger slips into the shadows as if to hide his identity and begins to speak softly. "
        "'There is a way out you know, a way to change all of this' he whispers. "
        "'A way to go back, back before the world we live in now and prevent 'this' future from ever happening.'"
    ]
    visitor_audio = "visitor.mp3"
    print_formatted_paragraphs(visitor_text, speak_enabled, visitor_audio)
    return make_choice("Do you:", ["Listen to the stranger", "Ignore the offer and stay in the cell"])
   
def listen_to_stranger(speak_enabled):                          ### Listen to stranger content
    listen_paragraph = [
        "The stranger's voice becomes barely audible as if the walls are listening. 'It is said that long ago, Aarondor was a land of prosperity, "
        "ruled by wise kings and queens. It is believed that the curse that befalls Aarondor today was born from an ancient relic. "
        "This relic, shrouded in legend and whispers, was sought by a ruler only known in our history as the ancient king, a ruler whose ambition turned to madness. "
        "He believed the relic would grant him immortality, but its power was far more sinister, twisting the fate of the entire kingdom.' "
        "You listen intently as he continues, 'The key to saving Aarondor lies in its past. The events that led to its downfall, the rise of the Ancient King, "
        "the quest for the ancient relic, all pivotal moments that forged our cursed reality. "
        "Your mission, should you choose to accept it, is to journey back and unravel these events, alter their course that you might prevent the kingdom's fall. "
        "But beware, the past is a tapestry woven with the threads of countless lives. Changing it could unravel realities in ways we cannot predict.'"
    ]
    listen_audio = "listen.mp3"
    print_formatted_paragraphs(listen_paragraph, speak_enabled, listen_audio)
    
def declining_choice(speak_enabled):                            ### Utility decline choice response
    declining_text = [
        "You decide to ignore the offer thinking it is meant to torture you into thinking there is a way out. Months blend into years, "
        "and your hope fades into the darkness of the cell. At last your suffering comes to end, right before you pass into oblivion you think "
        "'what might have been.'"
    ]
    decline_audio = "decline.mp3"
    print_formatted_paragraphs(declining_text, speak_enabled, decline_audio)
    input("\nPress Enter to continue...\n") 
    return False
    
def accept_mission(speak_enabled):                              ### Accept mission choice and Final decision choice
    paragraphs = [
        "The stranger reaches out passing the relic through the slot in the door as it glimmers in the dim light. "
        "'This armband is a relic from a time when our kingdom balanced on the edge of magic and machine. "
        "Only the high rulers were allowed to wield such power while denying it to the people,' he explains. "
        "As you reach out, a distant noise of a guard's movement echoes through the corridor. The stranger's eyes widen with urgency. "
        "'There is more to tell, but we have no time. It is now or never.'",
        
        "Make your choice!"
    ]
    accept_mission_audio = "accept.mp3"
    print_formatted_paragraphs(paragraphs, speak_enabled, accept_mission_audio)

### Final decision YES or NO choice
    final_decision = make_choice("Do you:", ["Take the armband and accept the mission", "Refuse and stay in your cell"])
    if final_decision == "1":
        final_decision_text_1 = [
            "With a mix of awe and apprehension, you slide the armband over your nervous hand. The band abruptly latches onto your forearm, "
            "its magic pulsing through your veins, it is a sensation like nothing you have ever felt before, both exhilarating and terrifying. "
            "You briefly think 'Oh no, what have I done.' In your previous life, when you were free, you had experimented with magic but nothing like this. "
            "This was far more powerful and alarming than anything you had ever experienced. Suddenly the armband begins to glow, "
            "the stranger is startled by the light of the band, as he steps back disappearing into the darkness he says "
            "'Remember the fait of Aarondor's present lies in your future."
        ]
        final_decision_audio_yes = "final_decision_yes.mp3"
        print_formatted_paragraphs(final_decision_text_1, speak_enabled, final_decision_audio_yes)
    elif final_decision == "2":
        final_decision_text_2 = [
            "Overwhelmed by the suddenness of the decision, you step back, declining the offer." 
            "The stranger vanishes into the shadows, "
            "leaving you alone in the silence once again."
        ]
        decline_final_audio_no = "final_decision_no.mp3"
        print_formatted_paragraphs(final_decision_text_2, speak_enabled, decline_final_audio_no)        
    else:
        print("\nUnrecognized choice. Please choose a valid option.")
        accept_mission()

    input("\nPress Enter to continue...\n")
   
def time_machine_explanation(speak_enabled):                    ### Time travel content
    time_machine_text = [
        "Curiosity piqued, you move closer. The stranger removes a small intricate device unlike anything you've ever seen - "
        "a perfect fusion of ancient craftsmanship and futuristic technology. "
        "This,' he begins, 'is not just a relic of the past, but a key to unlocking it. With this, you can change the past, altering the course of events that led us here. "
        "But there's a catch – if you go back, you can never return. As far as I can tell it's a one-way ticket,' he explains, "
        "his eyes locking with yours to emphasize the weight of his words. 'Your path forward will be in a reality you've rewritten. ",

        "The device, resembling an armband, is adorned with symbols that glow faintly, it is covered in ancient runes and symbols you have never seen, "
        "it's both beautiful and terrifying all at once. The stranger continues, 'It's powered by a rare combination of magic and advanced technology, lost to us now. "
        "When activated, it will create a temporal rift, a doorway to a pivotal moment in our history. But once you step through, the rift will close forever, "
        "leaving no way back to the present. ",

        "The journey will be perilous, and the consequences of your actions unpredictable. "
        "History is a delicate tapestry, and altering its threads could unravel realities in ways beyond our understanding. "
        "This mission, should you choose to accept it, is a leap into the unknown, a gamble with time itself."
    ]
    time_machine_audio = "time_machine.mp3"
    print_formatted_paragraphs(time_machine_text, speak_enabled, time_machine_audio)
    
    return make_choice("Do you:", ["Accept the one-way mission", "Refuse and stay in the present"])

def end_of_chapter_one(speak_enabled):                          ### End of chapter cliff hanger content
    end_of_chapter_text = [
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
    ]
    end_chapter_audio = "chapter_end.mp3"
    print_formatted_paragraphs(end_of_chapter_text, speak_enabled, end_chapter_audio)
#
# Primary code/function call
#
def chapter_one(speak_enabled):                                 ### Primary utility function call
    introduction(speak_enabled)
    cell_description(speak_enabled)
    while True:
        visitor_choice = mysterious_visitor(speak_enabled)
        if visitor_choice == '1':
            listen_to_stranger(speak_enabled)
            time_machine_choice = time_machine_explanation(speak_enabled)
            if time_machine_choice == '1':
                accept_mission(speak_enabled)
                return True
            elif time_machine_choice == '2':
                declining_choice(speak_enabled)
                return False  # End the story after declining
        elif visitor_choice == '2':
            declining_choice(speak_enabled)
            return False  # End the story after declining

def main():  
    print()                                                   ### Main function call
    print("KRONUS GATE")
    print()
    print("Chapter One")
    print()
    speak_enabled = get_user_choice_speak()
    print()
    #print(f"Speak Enabled: {speak_enabled}")
    if chapter_one(speak_enabled):  # Check if the story should proceed
        end_of_chapter_one(speak_enabled)
    else:
        print("\nThe story has ended. Thank you for playing.")

if __name__ == "__main__":
    main()
