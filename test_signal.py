import os
from dotenv import load_dotenv
from app import signal_groq

load_dotenv()

# Test 1: Clearly AI-generated
ai_text = "Artificial intelligence represents a transformative paradigm shift in modern society. It is important to note that while the benefits of AI are numerous, it is equally essential to consider the ethical implications."

# Test 2: Clearly human-written
human_text = "ok so i finally tried that new ramen place downtown and honestly? underwhelming. the broth was fine but they put WAY too much sodium in it and i was thirsty for like three hours after."

print("AI text score:", signal_groq(ai_text))
print("Human text score:", signal_groq(human_text))