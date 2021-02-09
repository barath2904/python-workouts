check_string = "hellogoodhellogoodhellogoodhello"
sub_string = "hellogoodhello"
# check occurrence of substring
# fetches overlapping count as well
occurrence_type1 = 0
occurrence_index_list = []
for i in range(len(check_string)):
    if check_string.startswith(sub_string, i):
        occurrence_type1 += 1
        occurrence_index_list.append(i)
print(occurrence_type1)
# gets indices of occurrences as well
print(occurrence_index_list)

# returns non-overlapping count
print(check_string.count(sub_string))

# --------------------------------------------------------------------------------------------------------------------
char_freq = {}
for char in check_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
max_char = max(char_freq)
print(F"max occurred character: '{max_char}, Occurrence: {char_freq[max_char]}")

# using counter approach
from collections import Counter
char_counter = Counter(check_string).items()
print(max(char_counter))

# --------------------------------------------------------------------------------------------------------------------


