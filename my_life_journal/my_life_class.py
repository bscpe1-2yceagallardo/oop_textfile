class MyLifeArchives:
    def __init__(self, archive_name="mylife.txt"):
        self.archive_name = archive_name
        self.lines_commited = 0
        # Verse Library for God's Affirmation
        self.bible_verses = {
            "happy": [
                "Psalms 118:24 - 'This is the day the Lord has made; let us rejoice and be glad in it.'",
                "Proverbs 17:22 - 'A chherful heart is good medicine.'",
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