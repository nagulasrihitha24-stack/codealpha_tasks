import random
words = ["python", "apple", "banana", "computer", "school"]
word = random.choice(words)
guessed_letters = []
chances = 6
print("=== Welcome to Hang Man ===")
while chances > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
    else:
        chances -= 1
        print("Wrong guess!")
        print("Remaining chances:", chances)
if chances == 0:
    print("\nYou lost!")
    print("The correct word was:", word)