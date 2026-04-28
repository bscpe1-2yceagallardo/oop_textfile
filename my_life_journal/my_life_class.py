import datetime
import random

class MyLifeArchives:
    def __init__(self, archive_name="mylife.txt"):
        self.archive_name = archive_name
        self.lines_committed = 0
        # Verse Library for God's Affirmation
        self.bible_verses = {
            "happy": [
                "Psalms 118:24 - 'This is the day the Lord has made; let us rejoice and be glad in it.'",
                "Proverbs 17:22 - 'A cheerful heart is good medicine.'",
                "Philippians 4:4 - 'Rejoice in the Lord always. I will say it again: Rejoice!'"
            ],
            "sad": [
                "Psalms 34:18 - 'The Lord is close to the brokenhearted and saves those who are crushed in spirit.'",
                "Matthew 5:4 - 'Blessed are those who mourn, for they will be comforted.'",
                "Joshua 1:9 - 'Do not be afraid; do not be discourage, for the Lord your God will be with you wherever you go.'"
            ],
            "general": [
                "Philippians 4:13 - 'I can do all things through Christ who strengthens me.'",
                "Jeremiah 29:11 - 'For I know the plans I have for you, declares the Lord.'"
            ]
        }

    def open_journal(self):
        author_identity = input("Identify yourself, Author:").strip() or "Dreamer"

        mood_input = input(f"Hello {author_identity}, how are you feeling at the moment? (happy/sad): ").lower().strip

        if mood_input == "happy":
            greeting = "That's Wonderful! Let's capture that sunshine! ☀️"
            visual_border = "✨ 💖 ✨ 💖 ✨ 💖 ✨"
        elif mood_input == "sad":
            greeting = "I'm sorry you're feeling down. I'm here to listen. 🌧️"
            visual_border = "--- 🕊️ --- 🕊️ --- 🕊️ ---"
        else:
            greeting = "I see. Let's get your thoughts down."
            visual_border = "-----------------------"
            mood_input = "general" # Default for verses

        print(greeting)

        try:
            with open(self.archive_name, "a", encoding="utf-8") as journal_file:
                # Timestamp
                session_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                journal_file.write(f"\n---SESSION START: {session_start} | MOOD: {mood_input.upper()}---\n")

                is_active = True
                while is_active:
                    user_text = input("Enter line: ")
                    entry_time = datetime.datetime.now().strftime("%H:%M:%S")

                    # Intensity Tagging
                    intensity = "[DEEP THOUGHT]" if len(user_text) > 50 else "[QUICK NOTE]"

                    formatted_line = f"{visual_border}\n[{entry_time}] {intensity} {author_identity}: {user_text}\n"
                    journal_file.write(formatted_line)
                    self.lines_committed += 1

                    if input("Add more? y/n: ").lower() != 'y':
                        is_active = False

                # Select verse based on mood
                verse_of_the_day = random.choice(self.bible_verses.get(mood_input, self.bible_verses["general"]))

                # Checksum Footer
                footer = (
                    f"---SESSION CLOSED---\n"
                    f"COMMITED: {self.lines_committed} lines\n"
                    f"MEDITATION: {verse_of_the_day}\n"
                )
                journal_file.write(footer)

            print(f"\n📖 Your Motivation: {verse_of_the_day}")
            print(f"🌟{self.lines_committed} entries saved. Your feelings are safe with me. Goodbye! 🌟")

        except IOError as error:
            print(f"❌ Error saving to disk: {error}")