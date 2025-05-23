import tkinter as tk
import random

# Score variables
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        result = f"You chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        computer_score += 1
        result = f"You chose {user_choice}, computer chose {computer_choice}. You lose!"

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.config(bg="#f0f0f0")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

for choice in ["rock", "paper", "scissors"]:
    tk.Button(button_frame, text=choice.capitalize(), font=("Helvetica", 12),
              width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", bg="#f0f0f0")
result_label.pack(pady=20)

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

root.mainloop()