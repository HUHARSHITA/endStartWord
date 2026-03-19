import random as r
import time
from english_words import get_english_words_set

word_set = get_english_words_set(['web2'], lower=True)

def is_valid(word, start, end):
    return (
        word in word_set and
        word.startswith(start.lower()) and
        word.endswith(end.lower())
    )

def main():
    print("🎮 WORD DUEL - SPEED EDITION 🎮")
    print("="*45)

    p1 = input("Enter Player 1 name: ").strip()
    p2 = input("Enter Player 2 name: ").strip()

    rounds = int(input("Enter number of rounds: "))

    score1 = 0
    score2 = 0

    for i in range(1, rounds + 1):
        print(f"\n🔥 ROUND {i} 🔥")

        start = chr(r.randint(65, 90))
        end = chr(r.randint(65, 90))

        print(f"Start Letter: {start}")
        print(f"End Letter: {end}")

        # Player 1 timing
        print(f"\n⏱️ {p1}, your turn...")
        t1_start = time.time()
        w1 = input("Enter word: ").lower().strip()
        t1_end = time.time()
        time1 = t1_end - t1_start

        # Player 2 timing
        print(f"\n⏱️ {p2}, your turn...")
        t2_start = time.time()
        w2 = input("Enter word: ").lower().strip()
        t2_end = time.time()
        time2 = t2_end - t2_start

        print(f"\n⏳ {p1} took {time1:.2f} sec")
        print(f"⏳ {p2} took {time2:.2f} sec")

        # Same word check
        if w1 == w2:
            print("⚠️ Same word entered! No points.")
            continue

        v1 = is_valid(w1, start, end)
        v2 = is_valid(w2, start, end)

        if v1 and not v2:
            score1 += 1
            print(f"🏆 {p1} gets the point!")
        elif v2 and not v1:
            score2 += 1
            print(f"🏆 {p2} gets the point!")

        elif v1 and v2:
            print("⚡ Both correct! Speed decides...")

            if time1 < time2:
                score1 += 1
                print(f"🚀 {p1} was faster and wins the round!")
            elif time2 < time1:
                score2 += 1
                print(f"🚀 {p2} was faster and wins the round!")
            else:
                print("🤝 Perfect tie! Both get points!")
                score1 += 1
                score2 += 1

        else:
            print("❌ Both incorrect! No points.")

        # Scoreboard
        print("\n📊 SCOREBOARD")
        print(f"{p1}: {score1}")
        print(f"{p2}: {score2}")

    # Final result
    print("\n🎉 FINAL RESULT 🎉")
    print(f"{p1}: {score1} | {p2}: {score2}")

    if score1 > score2:
        print(f"👑 {p1} wins!")
    elif score2 > score1:
        print(f"👑 {p2} wins!")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    main()
