# Story Content

class Story_Content:
    def __init__(self):
        pass

    def introduction(self):                                ### Introduction to the story
        text = [       
            "The once great Kingdom of Aarondor is now just a shadow of its former self. "
            "Torn apart by corruption and despair the people have lost all hope that things will get better. "
            "You have been imprisoned for opposing the tyrannical rule that has engulfed the land for centuries. "
            "Your mistake was searching for lost relics that could lift the ancient curse and overthrow the ruling class, you have been imprisoned and forgotten. "
            "The months have turned into years with only the memories of a life once lived and the company of your thoughts echoing in the silence."
        ]
        audio = "intro.mp3"
        return text, audio, None

    def cell_description(self):                            ### Prison cell description content
        text = [
            "Every day is the same, you wake up in a cold dark prison cell. The cell is small, with walls of unyielding stone, and always damp. "
            "Between the darkness and the cold, with nothing but the floor for a bed, you think, 'If there is such thing as hell, I have found it.' "
            "Death would be a kindness. In the endless silence, and darkness, the only light you have filters in through a tiny window high up on the wall. "
            "The door is solid metal and has seldom opened in the years you have been here. With only a small slot at eye level, you know very little of the world beyond."
        ]
        audio = "cell.mp3"
        return text, audio, None

    def mysterious_visitor(self):                          ### Mysterious Visitor 1st encounter
        text = [
            "As you ponder your life or rather, what is left of it, you hear the slot on the door slide open. "
            "You peer out trying to focus in the darkness and are met with a strangely familiar pair of eyes. "
            "Although you can't quite place where you have seen these eyes before the lines on his face tell a tale of a life fully lived. "
            "You can't help but think you must have met this stranger in a previous life. "
            "The stranger slips into the shadows as if to hide his identity and begins to speak softly. "
            "'There is a way out you know, a way to change all of this' he whispers. "
            "'A way to go back, back before the world we live in now and prevent 'this' future from ever happening.'"
        ]
        audio = "visitor.mp3"
        choices = ("Do you:", ["Listen to the stranger", "Ignore the offer and stay in the cell"])
        return text, audio, choices

    def listen_to_stranger(self):                          ### Listen to stranger content
        text = [
            "The stranger's voice becomes barely audible as if the walls are listening. 'It is said that long ago, Aarondor was a land of prosperity, "
            "ruled by wise kings and queens. It is believed that the curse that befalls Aarondor today was born from an ancient relic. "
            "This relic, shrouded in legend and whispers, was sought by a ruler only known in our history as the ancient king, a ruler whose ambition turned to madness. "
            "He believed the relic would grant him immortality, but its power was far more sinister, twisting the fate of the entire kingdom.' "
            "You listen intently as he continues, 'The key to saving Aarondor lies in its past. The events that led to its downfall, the rise of the Ancient King, "
            "the quest for the ancient relic, all pivotal moments that forged our cursed reality. "
            "Your mission, should you choose to accept it, is to journey back and unravel these events, alter their course that you might prevent the kingdom's fall. "
            "But beware, the past is a tapestry woven with the threads of countless lives. Changing it could unravel realities in ways we cannot predict.'"
        ]
        audio = "listen.mp3"
        return text, audio, None
    
    def declining_choice(self):                            ### Utility decline choice response
        text = [
            "You decide to ignore the offer thinking it is meant to torture you into thinking there is a way out. Months blend into years, "
            "and your hope fades into the darkness of the cell. At last your suffering comes to end, right before you pass into oblivion you think "
            "'what might have been.'"
        ]
        audio = "decline.mp3"
        return text, audio, None
        
    def time_machine_explanation(self):                    ### Time travel content
        text = [
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
        audio = "time_machine.mp3"
        choices = ("Do you:", ["Accept the one-way mission", "Refuse and stay in the present"])
        return text, audio, choices
    
    def accept_mission(self):                              ### Accept mission choice
        text = [
            "The stranger reaches out passing the relic through the slot in the door as it glimmers in the dim light. "
            "'This armband is a relic from a time when our kingdom balanced on the edge of magic and machine. "
            "Only the high rulers were allowed to wield such power while denying it to the people,' he explains. "
            "As you reach out, a distant noise of a guard's movement echoes through the corridor. The stranger's eyes widen with urgency. "
            "'There is more to tell, but we have no time. It is now or never.'",
            
            "Make your choice!"
        ]
        audio = "accept.mp3"
        choices = ("Do you:", ["Take the armband and accept the mission", "Refuse and stay in your cell"])
        return text, audio, choices

    def decline_mission(self):                             ### Decline mission choice
        text = [
            "Overwhelmed by the suddenness of the decision, you step back, declining the offer." 
            "The stranger vanishes into the shadows, "
            "leaving you alone in the silence once again."
        ]
        audio = "final_decision_no.mp3"
        return text, audio, None   

    def end_of_chapter_one(self):                          ### End of chapter cliff hanger content
        text = [
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
        audio = "chapter_end.mp3"
        return text, audio, None