import time
import textwrap
import threading
from playsound import playsound
from story_content_class_1 import StoryContent1

class StoryTeller:
    def __init__(self):
        self.speak_enabled = False

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

    def print_formatted_paragraphs(self, paragraphs, audio_file):
        audio_thread = self.play_audio_once(audio_file)
    
        for paragraph in paragraphs:
            wrapped_text = textwrap.fill(paragraph, width=100)
            self.slow_print(wrapped_text)
            print()
    
        if audio_thread:
            audio_thread.join()

    def slow_print(self, text):
        for character in text:
            print(character, end='', flush=True)
            time.sleep(.0625)
        print()

    def get_user_choice_speak(self):
        while True:
            choice = input("Would you like the story to be read aloud to you? (yes/no): ").strip().lower()
            print()
            if choice in ["yes", "y"]:
                self.speak_enabled = True
                return
            elif choice in ["no", "n"]:
                self.speak_enabled = False
                return
            else:
                print("Invalid choice. Please enter yes | no ")

    def make_choice(self, prompt, options):
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

    def play_story(self):
        print()                                                   
        print("KRONUS GATE")
        print()
        print("Chapter One")
        print()
        self.get_user_choice_speak()
        print()
        self.print_formatted_paragraphs(StoryContent1.introduction_text, "intro.mp3")
        self.print_formatted_paragraphs(StoryContent1.cell_description_text, "cell.mp3")
        choice = StoryContent1.mysterious_visitor(self.speak_enabled)
        if choice == "1":
            self.print_formatted_paragraphs(StoryContent1.listen_paragraph_text, "listen.mp3")
        else:
            self.print_formatted_paragraphs(StoryContent1.declining_text, "decline.mp3")
        self.print_formatted_paragraphs(StoryContent1.accept_mission_text, "accept.mp3")
        self.print_formatted_paragraphs(StoryContent1.time_machine_text, "time_machine.mp3")
        self.print_formatted_paragraphs(StoryContent1.end_of_chapter_text, "chapter_end.mp3")

if __name__ == "__main__":
    storyteller = StoryTeller()
    storyteller.play_story()
