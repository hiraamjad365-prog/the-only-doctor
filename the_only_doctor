# main.py - The Only Doctor Core Game Loop

def run_game():
    print("\n=== THE ONLY DOCTOR: BLACKWOOD'S PHYSICIAN ===")
    print("You are the sole doctor in an isolated town cut off by a winter storm.\n")
    
    integrity = 50
    print(f"Current Physician Integrity: {integrity}/100")
    print("---------------------------------------------")
    
    print("DILEMMA 1: A severe flu breakout has hit the town. Your medicine supply is dangerously low.")
    print("1. Ration the medicine equally among everyone, giving everyone a low chance of recovery.")
    print("2. Save the remaining medicine entirely for the town's children and elderly.")
    print("3. Give the medicine to the mayor and town council first to maintain local order.")
    
    choice = input("\nChoose your action (1, 2, or 3): ")
    
    if choice == "1":
        integrity += 10
        print("\nResult: You chose absolute fairness. Your integrity rises, but many remain sick.")
    elif choice == "2":
        integrity += 5
        print("\nResult: You protected the vulnerable. The town respects your compassion.")
    else:
        integrity -= 20
        print("\nResult: You favored political power. The town grows angry and distrustful.")
        
    print(f"\nFinal Physician Integrity: {integrity}/100")
    print("\n=== GAME OVER ===")
    print("Thank you for playing the Code in Place 2026 Showcase Demo!")

if __name__ == "__main__":
    run_game()
