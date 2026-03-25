import time

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def run_quiz():
    print_colored("\n🧠 --- REVISION QUIZ MODE ---", "1;35")
    score = 0
    questions = [
        {"q": "How do you stage all files for a commit?", "a": "git add ."},
        {"q": "What command temporarily hides your half-finished work?", "a": "git stash"},
        {"q": "How do you change the message of your very last commit?", "a": "git commit --amend"},
        {"q": "What command creates a new branch and switches to it?", "a": "git switch -c"}
    ]
    
    for item in questions:
        print(f"\nQuestion: {item['q']}")
        ans = input("Your command: ").strip()
        if ans == item['a'] or (item['a'] in ans and len(ans) > 3):
            print_colored("✅ Correct!", "1;32")
            score += 1
        else:
            print_colored(f"❌ Incorrect. The answer is: {item['a']}", "1;31")
            
    print_colored(f"\n🏆 Quiz Complete! Score: {score}/{len(questions)}", "1;36")
    time.sleep(2)

def main():
    print_colored("\n🚀 Welcome to the Git Master Guide!", "1;36")
    
    options = {
        "1": "Cheat Sheet: Starting or cloning",
        "2": "Cheat Sheet: Daily save loop",
        "3": "Cheat Sheet: Branching & Teamwork",
        "4": "Cheat Sheet: EMERGENCIES (Undo!)",
        "5": "Take the Revision Quiz",
        "6": "Exit"
    }

    while True:
        print("\n" + "-"*40)
        for key, val in options.items():
            print_colored(f"[{key}] {val}", "1;33")
        
        choice = input("\nEnter a number (1-6): ")

        if choice == '1':
            print_colored("\n--- SETUP & CLONING ---", "1;32")
            print("Start fresh: git init")
            print("Clone repo:  git clone <URL>")
        elif choice == '2':
            print_colored("\n--- DAILY LOOP ---", "1;32")
            print("See changes: git status\nStage files: git add .\nSave locally: git commit -m 'msg'\nUpload code: git push origin main")
        elif choice == '3':
            print_colored("\n--- BRANCHING ---", "1;32")
            print("Create & switch: git switch -c <name>\nMerge to main: git merge <name>")
        elif choice == '4':
            print_colored("\n--- EMERGENCIES ---", "1;31")
            print("Trash unsaved: git restore .\nHide work: git stash\nFind deleted: git reflog")
        elif choice == '5':
            run_quiz()
        elif choice == '6':
            print_colored("\nHappy coding! 💻\n", "1;36")
            break
        else:
            print_colored("Invalid choice. Try again.", "1;31")

if __name__ == "__main__":
    main()