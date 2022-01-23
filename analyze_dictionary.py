# Analyze entire dictionary to get 5 letter words

dict_filename = 'all_words.txt'
five_letter_dict_filename = 'five_letter_words.txt'

dict_file = open(dict_filename, 'r')
five_letter_dict_file = open(five_letter_dict_filename, 'w')

word_curr = True

while word_curr:
    word_curr = dict_file.readline()[:-1] # ignore newline character

    if len(word_curr) == 5:
        five_letter_dict_file.write(word_curr + '\n')

dict_file.close();
