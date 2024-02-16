# import dependencies
import time
import textwrap
import threading
from playsound import playsound
from story_content_class_1 import Story_Content

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
            time.sleep(.0125) # .0625 is the best setting for a good reading speed
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
    
    # Initialize Story_Content and Story_Teller
    story_content = Story_Content()
    story_teller = Story_Teller(story_content)

    # Enable or disable audio narration based on user choice
    story_teller.speak_enabled = story_teller.get_user_choice_speak()

    # This is where addition story parts can be added and called based on user choices to combine our two stories
    #text, audio, _ = story_content.thank_elf()
    #story_teller.print_formatted_paragraphs(text, audio)   
    
  #listen to space crash intro
    text, audio, _ = story_content.listen_to_space_crash()
    story_teller.print_fromatted_paragraphs(text, audio)

    if decision == 1:
        #thank elf
        text, audio, _ = story_content.thank_elf()
        story_teller.print_formatted_paragraphs(text, audio)
    
    elif decision == 2:
        #escape window
        text, audio, _ = story_content.escape_window()
        story_teller.print_formatted_paragraphs(text, audio)
        print("The story has ended. Thank you for playing.")
        return
    
    #thank elf
    text, audio, _ = story_content.thank_elf()
    story_teller.print_formatted_paragraphs(text, audio)

    if decision == 1:
        #speak to governor
        text, audio, _ = story_content.speak_to_governor()
        story_teller.print_formatted_paragraphs(text, audio)

    elif decision == 2:
        #decline governor
        text, audio, _ = story_content.listen_to_decline_fight()
        story_teller.print_formatted_paragraphs(text, audio)
    

    #escape window
    # text, audio, _ = story_content.escape_window()
    # story_teller.print_formatted_paragraphs(text, audio)
    # print("The story has ended. Thank you for playing.")

    #speak to governor 
    text, audio, _ = story_content.speak_to_governor()
    story_teller.print_formatted_paragraphs(text, audio)

    if decision == 1:
        #fight orcs then go to jail    
        text, audio, _ = story_content.fight_orcs_then_go_to_jail()
        story_teller.print_formatted_paragraphs(text, audio)
    
    elif decision == 2:
        # decline orc fight then go to jail 
        text, audio, _ = story_content.decline_orc_fight_then_go_to_jail()
        story_teller.print_formatted_paragraphs(text, audio)


    # Introduction
    text, audio, _ = story_content.introduction()
    story_teller.print_formatted_paragraphs(text, audio)
    
    # Cell Description
    text, audio, _ = story_content.cell_description()
    story_teller.print_formatted_paragraphs(text, audio)
    
    # Mysterious Visitor with a choice
    text, audio, choices = story_content.mysterious_visitor()
    story_teller.print_formatted_paragraphs(text, audio)
    decision = story_teller.make_choice(*choices)
    
    if decision == 1:
        # Listen to Stranger
        text, audio, _ = story_content.listen_to_stranger()
        story_teller.print_formatted_paragraphs(text, audio)

    elif decision == 2:
        # Decline the offer
        text, audio, _ = story_content.declining_choice()
        story_teller.print_formatted_paragraphs(text, audio)
        # After declining, conclude the story or prompt for restart/end
        print("The story has ended. Thank you for playing.")
        return  # Exit the main function to end the story

    # Time Machine Explanation with a choice
    text, audio, choices = story_content.time_machine_explanation()
    decision = story_teller.make_choice(*choices)

    if decision == 1:
        # Accept the mission
        text, audio, choices = story_content.accept_mission()  # Note: Now expecting choices to be part of the return
        story_teller.print_formatted_paragraphs(text, audio)
        if choices:  # Check if there are choices as part of accept_mission
            secondary_decision = story_teller.make_choice(*choices)
            if secondary_decision == 1:
                # Process the outcome of the first choice
                # Assuming there's a method to handle this path, e.g., mission_accepted
                text, audio, _ = story_content.end_of_chapter_one()  # Placeholder for actual method name
                story_teller.print_formatted_paragraphs(text, audio)
            elif secondary_decision == 2:
                # Process the outcome of the second choice
                # Assuming there's a method to handle this path, e.g., mission_declined
                text, audio, _ = story_content.decline_mission()  # Placeholder for actual method name
                story_teller.print_formatted_paragraphs(text, audio)
                # After declining, conclude the story or prompt for restart/end
                print("The story has ended. Thank you for playing.")
                return  # Exit the main function to end the story
    elif decision == 2:
        # Decline the mission
        text, audio, _ = story_content.decline_mission()
        story_teller.print_formatted_paragraphs(text, audio)
        # After declining, conclude the story or prompt for restart/end
        print("The story has ended. Thank you for playing.")
        return  # Exit the main function to end the story

    

if __name__ == "__main__":
    main()