# Hi there 👋 I'm Ryougaa Hideki

from datetime import datetime

class AboutMe:
    def __init__(self):
        self.name = "Ryougaa Hideki"
        self.username = "n1k4xryougaaa"
        self.birth_year = 2009
        self.age = datetime.now().year - self.birth_year
        self.language = ["Python", "Bash", "JavaScript"]
        self.interests = ["Automation", "Obfuscation", "Cybersecurity"]
        self.hobby = ["Listening to Lofi 🎧", "Coding at night 🌙"]

    def contact(self):
        socials = {
            "🌐 Website"   : "https://n1k4xryougaaa.github.io",
            "🐙 GitHub"    : "https://github.com/n1k4xryougaaa",
            "📸 Instagram" : "https://instagram.com/v3n.ryougaa",
            "▶️ YouTube"   : "https://youtube.com/@lynntheurprince",
            "💬 Telegram"  : "https://t.me/yourusername"
        }
        return socials

me = AboutMe()
print(f"Hi, I'm {me.name}, {me.age} years old! 🚀")
print("Feel free to explore my repositories and connect with me online ✨")
