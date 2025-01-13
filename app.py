'''Python Functions - Data Structure Exercise'''

SENTENCE = "This is a common interview question"

char_frequency = {}

for char in SENTENCE:
    if char in char_frequency:
        # iterates over SENTENCE converting it into a dictionary and
        # if the character appears in the dict it increments the value by 1
        char_frequency[char] += 1
    else:
        # otherwise add it to the dictionary and the value is set to 1
        char_frequency[char] = 1
#  the dictonary items are put into a list of tuples and
# then sorted in reverse showing the most common letter first
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

most_common_char = char_frequency_sorted[0]

print(
    f"The most common letter {most_common_char[0]} appears {most_common_char[1]} times in SENTENCE")
