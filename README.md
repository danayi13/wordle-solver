# wordle-solver
program to help solve the popular puzzle from [wordleunlimited.com](wordleunlimited.com)

## Plan:
### Prep + Analysis
1. Get list of all English words from [here](https://github.com/dwyl/english-words)
2. Analyze above to get list of all 5 letter words in English
3. Do analysis about frequency/placement of letters
- What letter appear most frequently?
- What letter appears in each location most frequently?
- When letters appear, in which location do they most frequently appear?
4. Implement simple CLI for user to interact with

### Game Strategy
- Guess 'adieu' as the first word
- Rank the possible subsequent suggestions by
  - How many new letters it introduces
  - How common the letters it introduces are
  - How common the letters it has in each position are
  - How many words the guess would remove based on each possible response

## File Outline:
`all_words.txt` - list of all words in the English language

`analysis.txt` - output of anayzing five-letter-words

`analyze_dictionary.py` - use all English words to create file of all 5 letter words

`analyze_five_letter.py` - analyze frequency/placement of letters for 5 letter words

`five_letter_words.txt` - all 5 letter English words

`solve_wordle.py` - run this file to have an interactive wordle solver/suggestions
