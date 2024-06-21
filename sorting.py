# Author: Natalia Tam

# Define input and output file paths
input_file = '/Users/net02/Documents/Workspace/ScrabbleProject/words.txt'
output_file2 = '2_letter_words.txt' 
output_file3 = '3_letter_words.txt'
output_file4 = '4_letter_words.txt' 
output_file5 = '5_letter_words.txt' 
output_file6 = '6_letter_words.txt' 
output_file7 = '7_letter_words.txt' 

# Open input file for reading
with open(input_file, 'r') as f_input:
    words = f_input.read().splitlines()

print("Step 1 completed.")

# Filter out 3-letter words
two_letter_words = [word for word in words if len(word) == 2]
three_letter_words = [word for word in words if len(word) == 3]
four_letter_words = [word for word in words if len(word) == 4]
five_letter_words = [word for word in words if len(word) == 5]
six_letter_words = [word for word in words if len(word) == 6]
seven_letter_words = [word for word in words if len(word) == 7]

print("Step 2 completed.")

# Open output file for writing
with open(output_file2, 'w') as f_output:
    # Write each 2-letter words to the output file
    for word in two_letter_words:
        f_output.write(word + '\n')

with open(output_file3, 'w') as f_output:
    for word in three_letter_words:
        f_output.write(word + '\n')
with open(output_file4, 'w') as f_output:
    for word in four_letter_words:
        f_output.write(word + '\n')
with open(output_file5, 'w') as f_output:
    for word in five_letter_words:
        f_output.write(word + '\n')
with open(output_file6, 'w') as f_output:
    for word in six_letter_words:
        f_output.write(word + '\n')
with open(output_file7, 'w') as f_output:
    for word in seven_letter_words:
        f_output.write(word + '\n')

print(f"Extracted {len(three_letter_words)} 3-letter words to {output_file3}.")