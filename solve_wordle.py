# Run this file to run the interactive wordle solver + suggestion

# Get all five letter words
five_letter_file = open('five_letter_words.txt')
five_letter_words = []
word_curr = True
while word_curr:
    word_curr = five_letter_file.readline()[:-1] # ignore newline character
    if len(word_curr) > 0: five_letter_words.append(word_curr) # ignore newline at eof
print("NUM POSSIBLE WORDS: " + str(len(five_letter_words)))

def letter_not_present(letter):
    global five_letter_words
    five_letter_words = list(filter(lambda x: letter not in x, five_letter_words))

def letter_correct(letter, index):
    global five_letter_words
    five_letter_words = list(filter(lambda x: x[index] == letter, five_letter_words))

def letter_present_wrong_spot(letter, index):
    global five_letter_words
    five_letter_words = list(filter(lambda x: x[index] != letter and letter in x, five_letter_words))

if __name__ == '__main__':
    print("Welcome to the Wordle Solver!")
    print("Guess 'ADIEU' as your first word.")
    current_guess = 'adieu'

    for _ in range(5):
        print("Input response (format with 'x' for no letter, 'o' for letter present in wrong spot, and 'y' for correct spot)")
        correctness = input("Response: ")
        for i in range(5):
            if correctness[i] == 'x':
                letter_not_present(current_guess[i])
            elif correctness[i] == 'y':
                letter_correct(current_guess[i], i)
            elif correctness[i] == 'o':
                letter_present_wrong_spot(current_guess[i], i)
        
        # TODO optimize possible words
        print("POSSIBLE WORDS: " + str(five_letter_words))
        print("POSSIBLE LIST LENGTH: " + str(len(five_letter_words)))

        current_guess = input("Guess another word: ")
            