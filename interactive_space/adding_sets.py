import time
import textwrap


class player_choice:
    def __init__(self):
        self.unique_choices = set()

    def make_unique_choice(self, prompt, options):
        while True:
            print("\n" + prompt)
            for number, option in enumerate(options, 1):
                print(f"{number}. {option}")
            choice = input("Enter your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                if choice not in self.unique_choices:
                    self.unique_choices.add(choice)
                    return int(choice)
                else:
                    print("You've already made that choice. Please choose a different option.")
            else:
                print("Invalid choice. Please enter a valid number.")

class Story_Teller:
    def __init__(self, story_content):
        self.story_content = story_content
        self.player_choice = player_choice()
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

    def print_formatted_paragraphs(self, paragraphs):
        for paragraph in paragraphs:
            wrapped_text = textwrap.fill(paragraph, width=100)
            self.slow_print(wrapped_text)
            print()

    def slow_print(self, text):
        for character in text:
            print(character, end='', flush=True)
            time.sleep(.0125) # .0625 is the best setting for a good reading speed
        print()

    def make_choice(self, prompt, options):
        return self.player_choice.make_unique_choice(prompt, options)

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
        text, choices = story_part()  # Extract content from the story part
        self.print_formatted_paragraphs(text)  # Display text

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
    
    

    # Enable or disable audio narration based on user choice
    story_teller.speak_enabled = story_teller.get_user_choice_speak()

    # This is where additional story parts can be added and called based on user choices to combine our two stories
    # For example:
    # story_teller.start_chapter('chapter_name')
    
    if __name__ == "__main__":
        main()
