# Analyze the five letter dictionary to get info
five_letter_filename = 'five_letter_words.txt'
five_letter_file = open(five_letter_filename, 'r')

# populate python dict
five_letter_words = []
word_curr = True
while word_curr:
    word_curr = five_letter_file.readline()[:-1] # ignore newline character
    if len(word_curr) > 0: five_letter_words.append(word_curr) # ignore newline at eof

# Analyze the most common letters
print("Most Frequent Letters:")
letter_to_frequency = {}
num_letters_tot = 0
for word in five_letter_words:
    for letter in word:
        num_letters_tot += 1
        if letter in letter_to_frequency:
            letter_to_frequency[letter] += 1
        else:
            letter_to_frequency[letter] = 1
letter_freq_list = sorted([(l, letter_to_frequency[l]) for l in letter_to_frequency], key=lambda x:x[1], reverse=True)

for (l, f) in letter_freq_list:
    print(f'letter: {l}, freq: {str(round(f * 100.0 / num_letters_tot, 2)):5}%')
print()

# Analyze the most frequency letters that show up per location
num_words = len(five_letter_words)
position_list = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
for i in range(5):
    print(f'Most Frequent Letter In The {position_list[i]} Position:')
    letter_to_freq = {}
    for word in five_letter_words:
        fst = word[i]
        if fst in letter_to_freq:
            letter_to_freq[fst] += 1
        else:
            letter_to_freq[fst] = 1
    letter_freq_list = sorted([(l, letter_to_freq[l]) for l in letter_to_freq], key=lambda x:x[1], reverse=True)

    for (l, f) in letter_freq_list:
        print(f'letter: {l}, freq: {str(round(f * 100.0 / num_words, 2)):5}%')
    print()

# Analyze the most common position per letter
chars = [chr(i) for i in range(97, 123)]

for c in chars:
    num_occur = 0
    pos_to_freq = {}
    for word in five_letter_words:
        for pos in range(5):
            letter = word[pos]
            if letter == c:
                num_occur += 1
                if pos in pos_to_freq:
                    pos_to_freq[pos] += 1
                else:
                    pos_to_freq[pos] = 1
    print(f'Most Frequent location for letter : {c}')
    pos_freq_list = sorted([(l, pos_to_freq[l]) for l in pos_to_freq], key=lambda x:x[1], reverse=True)
    for (pos, l) in pos_freq_list:
        print(f'position: {pos+1}, freq: {str(round(l * 100.0 / num_occur, 2)):5}%')
    print()
