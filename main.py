 # main.py - The Only Doctor: Blackwood's Physician
# Final Project for Stanford Code in Place 2026

def get_ending(score):
    """Determines the player's professional title based on their integrity score."""
    print("\n=============================================")
    print("                 GAME OVER                   ")
    print("=============================================")
    print(f"Your Final Physician Integrity Score: {score}/100")
    
    if score >= 75:
        print("\nENDING: THE SAINT OF BLACKWOOD")
        print("You prioritized human life and medical ethics above all else.")
        print("The townspeople look up to you as a beacon of hope in the dark.")
    elif score >= 45:
        print("\nENDING: THE PRAGMATIC PHYSICIAN")
        print("You made tough choices and compromised when necessary to survive.")
        print("The town respects your realism, though your hands aren't entirely clean.")
    else:
        print("\nENDING: THE EXILED QUACK")
        print("You favored power, money, and self-preservation over your patients.")
        print("Once the winter storm clears, the town council banishes you into the mountains.")

def run_game():
    print("\n=== THE ONLY DOCTOR: BLACKWOOD'S PHYSICIAN ===")
    print("You are the sole doctor in an isolated town cut off by a winter storm.")
    print("Every choice you make impacts your Integrity Score. Choose wisely.\n")
    
    integrity = 50  # Starting mid-way
    
    # List of dilemmas: (Dilemma Text, Option 1, Option 2, Option 3, Score Changes)
    dilemmas = [
        {
            "text": "DILEMMA 1: A severe flu breakout hits Blackwood. Vaccine supplies are dangerously low.",
            "1": "Ration the medicine equally (Fairness: +10 Integrity)",
            "2": "Save it entirely for children and the elderly (Compassion: +5 Integrity)",
            "3": "Prioritize the Mayor and town council first (Political Favor: -15 Integrity)",
            "scores": [10, 5, -15]
        },
        {
            "text": "DILEMMA 2: A wealthy merchant offers a massive financial donation to your clinic, but demands you hide the fact that his son has a highly contagious outbreak.",
            "1": "Refuse the bribe and report the case immediately (Honesty: +15 Integrity)",
            "2": "Take the money secretly to buy better clinic supplies later (Compromise: -5 Integrity)",
            "3": "Take the bribe and prioritize treating his son privately (Corruption: -20 Integrity)",
            "scores": [15, -5, -20]
        },
        {
            "text": "DILEMMA 3: An injured fugitive bandit arrives at your clinic at midnight bleeding heavily. The town sheriff is outside searching for him.",
            "1": "Treat the patient completely before addressing the law (Medical Oath: +15 Integrity)",
            "2": "Hand him over to the sheriff immediately without treating him (Citizen Duty: -10 Integrity)",
            "3": "Patch him up quickly and demand all his stolen gold to stay quiet (Extortion: -25 Integrity)",
            "scores": [15, -10, -25]
        }
    ]

    # Game Loop to iterate through the scenarios
    for i, dilemma in enumerate(dilemmas):
        print(f"\n---------------------------------------------")
        print(f"CURRENT INTEGRITY: {integrity}/100")
        print(f"---------------------------------------------")
        print(dilemma["text"])
        print(f"1. {dilemma['1']}")
        print(f"2. {dilemma['2']}")
        print(f"3. {dilemma['3']}")
        
        # Input validation loop
        while True:
            choice = input("\nChoose your action (1, 2, or 3): ").strip()
            if choice in ["1", "2", "3"]:
                break
            print("Invalid input. Please enter 1, 2, or 3.")
            
        # Apply score changes based on the validated index
        idx = int(choice) - 1
        integrity += dilemma["scores"][idx]
        
        # Clamp score between 0 and 100
        integrity = max(0, min(integrity, 100))

    # Calculate final narrative ending
    get_ending(integrity)

if __name__ == "__main__":
    while True:
        run_game()
        replay = input("\nWould you like to try a different ethical path? (yes/no): ").lower().strip()
        if replay != 'yes' and replay != 'y':
            print("\nThank you for playing the Code in Place 2026 Showcase Entry!")
            break
