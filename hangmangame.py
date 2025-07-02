import random 
from wordlists import cs_words

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",   
                   "/  "),
               6: (" o ",
                   "/|\\",   
                   "/ \\") }

def display_hangman(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")
def display_hint(hint):
    print("  ".join(hint))

def display_answer(answer):
    print("  ".join(answer))




def main():
    answer = random.choice(cs_words)
    hint =["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    print("*******************************************************************************************")
    print("     Welcome to hangman game(Try to guess the word related to computer science field)      ")
    print("*******************************************************************************************")
    print()
    while is_running:
        display_hangman(wrong_guesses)
        print()
        
        display_hint(hint)
        print()
        
        guess = input("Enter a letter : ").lower()
        print()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input !")
            print()
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed !")
            print()
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if not "_" in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("You Won !")
            is_running = False
        elif wrong_guesses == len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("You Lost !")
            is_running = False

if __name__ == "__main__":
    main()