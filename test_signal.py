from app import signal_groq, signal_stylometric

ai_text = "Artificial intelligence represents a transformative paradigm shift in modern society. It is important to note that while the benefits of AI are numerous, it is equally essential to consider the ethical implications. Furthermore, stakeholders across various sectors must collaborate to ensure responsible deployment."

human_text = "ok so i finally tried that new ramen place downtown and honestly? underwhelming. the broth was fine but they put WAY too much sodium in it and i was thirsty for like three hours after. my friend got the spicy version and said it was better. probably won't go back unless someone drags me there"

print("=== AI text ===")
print("Groq score:", signal_groq(ai_text))
print("Stylometric score:", signal_stylometric(ai_text))

print("\n=== Human text ===")
print("Groq score:", signal_groq(human_text))
print("Stylometric score:", signal_stylometric(human_text))