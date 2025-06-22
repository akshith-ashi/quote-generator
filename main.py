import tkinter as tk
import random

quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else is going to do it for you.",
    "Do something today that your future self will thank you for.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Opportunities don’t happen. You create them.",
    "It always seems impossible until it’s done.",
    "Don’t wait for opportunity. Create it.",
    "The key to success is to focus on goals, not obstacles.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Success is what comes after you stop making excuses.",
    "Your limitation—it’s only your imagination.",
    "Sometimes later becomes never. Do it now.",
    "Dream it. Wish it. Do it.",
    "Stay focused and never give up.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Push harder than yesterday if you want a different tomorrow.",
    "Work until your idols become your rivals.",
    "Little things make big days.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t limit your challenges. Challenge your limits.",
    "You are capable of amazing things.",
    "Doubt kills more dreams than failure ever will.",
    "Start where you are. Use what you have. Do what you can.",
    "Great things take time. Be patient.",
    "Don’t be pushed around by the fears in your mind.",
    "Success is not for the lazy.",
    "Learn from yesterday. Live for today. Hope for tomorrow.",
    "Winners are not people who never fail, but people who never quit.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Try not to become a man of success, but rather try to become a man of value.",
    "Only I can change my life. No one can do it for me.",
    "Failure will never overtake me if my determination to succeed is strong enough.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "Perseverance is not a long race; it’s many short races one after the other.",
    "Make each day your masterpiece.",
    "The secret of getting ahead is getting started.",
    "Your only limit is your mind.",
    "Don’t tell people your plans. Show them your results.",
    "I can and I will. Watch me.",
    "Be stronger than your excuses.",
    "Discipline is doing what needs to be done even if you don’t want to.",
    "Success usually comes to those who are too busy to be looking for it.",
    "The best revenge is massive success.",
    "Act as if what you do makes a difference. It does.",
    "Don’t wish it were easier. Wish you were better.",
    "A year from now you may wish you had started today.",
    "You miss 100% of the shots you don’t take.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Believe you can and you’re halfway there.",
    "Go the extra mile. It’s never crowded.",
    "If it doesn’t challenge you, it won’t change you.",
    "Take the risk or lose the chance.",
    "The only way to do great work is to love what you do.",
    "Difficult roads often lead to beautiful destinations.",
    "Do not wait for the perfect moment. Take the moment and make it perfect.",
    "Success is not in what you have, but who you are.",
    "Don’t raise your voice. Improve your argument.",
    "You didn’t come this far to only come this far.",
    "Be so good they can’t ignore you.",
    "You are your only limit.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Small progress is still progress.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Don’t be afraid to start over. It’s a chance to build something better.",
    "Don't compare yourself to others. Compare yourself to the person from yesterday.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "The difference between who you are and who you want to be is what you do.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Never regret a day in your life: good days give happiness, bad days give experience.",
    "You don’t grow when you’re comfortable.",
    "Don't quit. Suffer now and live the rest of your life as a champion.",
    "If you want something you’ve never had, you must be willing to do something you’ve never done.",
    "Even if you fall on your face, you’re still moving forward.",
    "The man who moves a mountain begins by carrying away small stones.",
    "Success begins with self-discipline.",
    "Don't wait for opportunity. Create it.",
    "Do it now. Sometimes 'later' becomes 'never.'",
    "Strive for progress, not perfection.",
    "The future depends on what you do today.",
    "You don’t need to see the whole staircase. Just take the first step.",
    "Start small, think big. Don’t worry about too many things at once.",
    "Big journeys begin with small steps.",
    "The best way to predict the future is to create it.",
    "Mistakes are proof that you’re trying.",
    "Be proud of how hard you are trying.",
    "Fall seven times, stand up eight.",
    "Don’t count the days. Make the days count.",
    "When you feel like quitting, think about why you started.",
    "Don’t be afraid to give up the good to go for the great.",
    "No pressure, no diamonds.",
    "You are not a product of your circumstances. You are a product of your decisions.",
    "A little progress each day adds up to big results.",
    "Your dreams don’t work unless you do.",
    "Success isn’t just about what you accomplish, it’s about what you inspire others to do."
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

    heading = tk.Label(root, text=" Quote of the Day ", font=("Helvetica", 16, "bold"), bg="#f0f8ff")
    heading.pack(pady=20)

    quote_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12), bg="#f0f8ff", justify="center")
    quote_label.pack(pady=20)

    generate_button = tk.Button(root, text="Get Quote", command=generate_quote, font=("Arial", 12, "bold"), bg="#4682B4", fg="white", padx=10, pady=5)
    generate_button.pack()

    generate_quote()
    root.mainloop()

if __name__ == "__main__":
    run_app()


