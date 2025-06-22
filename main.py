import tkinter as tk
import random

quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else is going to do it for you.",
    "Do something today that your future self will thank you for.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

def generate_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

def run_app():
    global quote_label

    root = tk.Tk()
    root.title("Motivational Quote Generator")
    root.geometry("500x300")
    root.configure(bg="#f0f8ff")

    heading = tk.Label(root, text="🌟 Quote of the Day 🌟", font=("Helvetica", 16, "bold"), bg="#f0f8ff")
    heading.pack(pady=20)

    quote_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12), bg="#f0f8ff", justify="center")
    quote_label.pack(pady=20)

    generate_button = tk.Button(root, text="Get Quote", command=generate_quote, font=("Arial", 12, "bold"), bg="#4682B4", fg="white", padx=10, pady=5)
    generate_button.pack()

    generate_quote()
    root.mainloop()

if __name__ == "__main__":
    run_app()


