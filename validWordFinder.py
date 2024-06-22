from itertools import permutations

# Define input and output file paths
output_file4 = '4_letter_words.txt' 
output_file5 = '5_letter_words.txt' 
output_file6 = '6_letter_words.txt' 
output_file7 = '7_letter_words.txt' 

valid_seven = set()

# Open input file for reading
with open(output_file4, 'r') as f_input:
    four_words = f_input.read().splitlines()
    print("four_words reading complete")

# Open input file for reading
with open(output_file5, 'r') as f_input:
    five_words = f_input.read().splitlines()
    print("five_words reading complete")

# Open input file for reading
with open(output_file6, 'r') as f_input:
    six_words = f_input.read().splitlines()
    print("six_words reading complete")

# Open input file for reading
with open(output_file7, 'r') as f_input:
    seven_letter_words = f_input.read().splitlines()
    print("seven_words reading complete")

#-----------------------------------------------------------------------

# Function to find all words of a specific length that can be formed 
# from a given set of letters
def find_words_of_length(letters, word_length, valid_words):
    permutations_set = set([''.join(p) for p in permutations(letters, word_length)])
    valid_words_set = set(valid_words)
    found_words = sorted(list(permutations_set & valid_words_set))
    return found_words

#-----------------------------------------------------------------------
'''
# Open output file for writing
with open("valid_seven_letter_words", 'w') as f1, open("seven_and_six", 'w') as f2:

    # Iterate over each seven-letter word
    for seven_word in seven_letter_words:
        # Find all six-letter words that can be formed from the seven-letter word
        found_six = find_words_of_length(seven_word, 6, six_words)
        if len(found_six) >= 1: 
            f1.write(seven_word + '\n')
            f2.write(seven_word + '\n')
            for w in found_six:
                f2.write(w + '\n')
            f2.write('\n')
'''

#-----------------------------------------------------------------------

# Function to read words from a file and create tuples
def create_tuples_from_file(filename):
    tuples_list = []
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')

    i = 0
    while i < len(lines):
        seven_letter_word = lines[i]
        words = [seven_letter_word]
        i += 1
        #six_letter_words = []
        while i < len(lines) and lines[i].strip() != '':
            #six_letter_words.append(lines[i])
            words.append(lines[i])
            i += 1
        #tuples_list.append((seven_letter_word, tuple(six_letter_words)))
        tuples_list.append(words)
        i += 1  # Skip the blank line between groups
    return tuples_list

#-----------------------------------------------------------------------

filename = 'seven_and_six' 
word_tuples = create_tuples_from_file(filename)

# Open output file for writing
with open("valid_seven_letter_words", 'w') as f1, open("7_6_5", 'w') as f2:

    for tuples in word_tuples:
        for six_word in tuples[1:]:
            found_five = find_words_of_length(six_word, 5, five_words)
            if len(found_five) >= 1: 
                f1.write(tuples[0] + '\n')
                f2.write(tuples[0] + '\n' + six_word + '\n')
                for w in found_five:
                    f2.write(w + '\n')
                f2.write('\n')

print("done with 7 and 6 and 5's")


#-----------------------------------------------------------------------

filename = '7_6_5'
word_tuples = create_tuples_from_file(filename)

# Open output file for writing
with open("valid_seven", 'w') as f1, open("7_6_5_4", 'w') as f2:

    i = 0
    for tuples in word_tuples:
        if i % 1000 == 0:
            print(tuples[0])
        i += 1
        for five_word in tuples[2:]:
            found_four = find_words_of_length(five_word, 4, four_words)
            if len(found_four) >= 1: 
                if tuples[0] not in valid_seven:
                    f1.write(tuples[0] + '\n')
                    valid_seven.add(tuples[0])
                f2.write(tuples[0] + '\n' + tuples[1] + '\n' + five_word + '\n')
                print(five_word)
                for w in found_four:
                    f2.write(w + '\n')
                f2.write('\n')