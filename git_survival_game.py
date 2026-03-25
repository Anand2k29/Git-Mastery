import time
import os

# --- Helper Functions ---

def clear_screen():
    # This checks if your OS is Windows ('nt') or Mac/Linux. 
    # It runs the correct terminal command to clear the screen so the game looks clean.
    os.system('cls' if os.name == 'nt' else 'clear')

def print_color(text, color_code):
    # This uses ANSI escape codes to change the color of the text in the terminal.
    # "\033[" starts the color, "m" ends the color code, and "\033[0m" resets it to default.
    print(f"\033[{color_code}m{text}\033[0m")

# --- Main Game Logic ---

def play_game():
    clear_screen()
    print_color("=== 🎮 GIT SURVIVAL MODE ===", "1;35") # 1;35 is Purple
    print("You are a lead developer. Production is on fire.")
    print("Type the exact Git commands to survive the crises. Let's go!\n")
    
    # Pauses the game for 2 seconds for dramatic effect
    time.sleep(2)

    # We start the player with 0 points
    score = 0
    
    # This is a List of Dictionaries containing the questions and answers
    questions = [
        {
            "scenario": "CRISIS 1: You just wrote some brilliant code. Stage ALL changed files to prepare them for a save.",
            "answer": "git add ."
        },
        {
            "scenario": "CRISIS 2: Files are staged! Now, permanently save them locally. (Use any commit message).",
            "answer": "git commit -m" 
        },
        {
            "scenario": "CRISIS 3: Your new code is terrible. Destroy all unsaved changes and go back to the last clean save.",
            "answer": "git restore ."
        },
        {
            "scenario": "CRISIS 4: An urgent bug requires you to switch branches! Hide your half-finished work temporarily.",
            "answer": "git stash"
        },
        {
            "scenario": "CRISIS 5: Crisis averted! Check your project's history to ensure your commits are safe.",
            "answer": "git log"
        }
    ]

    # This loop goes through every question in the list one by one
    for q in questions:
        print_color(f"\n{q['scenario']}", "1;36") # 1;36 is Cyan
        
        # input() waits for the user to type something. 
        # .strip().lower() removes extra spaces and makes it lowercase to prevent unfair typos.
        user_input = input(">> Your Command: ").strip().lower()
        
        # We check if the correct answer is INSIDE whatever the user typed
        if q['answer'] in user_input:
            print_color("✅ CORRECT! Crisis managed.", "1;32") # 1;32 is Green
            score += 10 # Add 10 points
        else:
            print_color(f"💥 FATAL ERROR! The correct command was: {q['answer']}", "1;31") # 1;31 is Red
        
        time.sleep(1.5)

    # --- Endgame Results ---
    print_color("\n=== 🏁 GAME OVER ===", "1;35")
    print_color(f"Final Score: {score} / 50", "1;33") # 1;33 is Yellow
    
    # Ranking system based on the final score
    if score == 50:
        print_color("Rank: 👑 GIT MASTER - Flawless execution!", "1;32")
    elif score >= 30:
        print_color("Rank: 🛠️ SENIOR DEV - You survived, but it was close.", "1;36")
    else:
        print_color("Rank: 👶 INTERN - Back to the cheat sheet for you!", "1;31")

# --- Program Entry Point ---
# This tells Python to only run the game if this file is executed directly.
if __name__ == "__main__":
    play_game()