import itertools

# works only for list of list
# elements of parent list has to be list
# can flatten only one level
list_of_list = [[1, 2], [3, 4]]
merged_list = list(itertools.chain.from_iterable(list_of_list))
print(merged_list)

# flattening 2D list
nested_list = [2, [1, 2], 5, [3, 4]]
# nested_list = [1, [1, 1], 1, [1, 1, 1], 1, 1]
flatten_list = []
for elem in nested_list:
    if isinstance(elem, list):
        for item in elem:
            flatten_list.append(item)
    else:
        flatten_list.append(elem)
print(flatten_list)
