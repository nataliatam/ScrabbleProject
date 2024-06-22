#-----------------------------------------------------------------------
from itertools import permutations

# Define input and output file paths
output_file3 = '3_letter_words.txt' 
output_file4 = '4_letter_words.txt' 
output_file5 = '5_letter_words.txt' 
output_file6 = '6_letter_words.txt' 
output_file7 = '7_letter_words.txt' 

valid_seven = set()

# Open input file for reading
with open(output_file3, 'r') as f_input:
    three_words = f_input.read().splitlines()
    print("three_words reading complete")

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
#---
# --------------------------------------------------------------------

# Function to find all words of a specific length that can be formed 
# from a given set of letters
def find_words_of_length(letters, word_length, valid_words):
    permutations_set = set([''.join(p) for p in permutations(letters, word_length)])
    valid_words_set = set(valid_words)
    found_words = sorted(list(permutations_set & valid_words_set))
    return found_words


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

filename = '7_6_5_4 (first half)'
word_tuples = create_tuples_from_file(filename)

# Open output file for writing
with open("valid_seven1", 'w') as f1, open("7_6_5_4_3 first half", 'w') as f2:

    i = 0
    for tuples in word_tuples:
        if i % 1000 == 0:
            print(tuples[0])
        i += 1
        for four_word in tuples[3:]:
            found_three = find_words_of_length(four_word, 3, three_words)
            if len(found_three) >= 1: 
                if tuples[0] not in valid_seven:
                    f1.write(tuples[0] + '\n')
                    valid_seven.add(tuples[0])
                f2.write(tuples[0] + '\n' + tuples[1] + '\n' + tuples[2] + '\n' + four_word + '\n')
                # print(found_four)
                for w in found_three:
                    f2.write(w + '\n')
                f2.write('\n')