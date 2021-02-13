from collections import Counter

# check occurrence of substring in a string
check_string = "hellogoodhellogoodhellogoodhello"
sub_string = "hellogoodhello"
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
# check maximum occurrence of element in a string/list
char_freq = {}
list_val = [1, 2, 4, 5, 1, 2, 1]
string_val = check_string
for char in string_val:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
max_char = max(char_freq, key=char_freq.get)
print(F"max occurred character: '{max_char}', Occurrence: {char_freq[max_char]}")

# using counter approach
char_counter = Counter(check_string)
print(char_counter)
print(max(char_counter, key=char_counter.get))

list_counter = Counter([1, 2, 4, 5, 1, 2, 1])
print(list_counter)
print(max(list_counter, key=list_counter.get))
# --------------------------------------------------------------------------------------------------------------------


