import itertools

nested_list = [[1, 2], ["hi", "hello"], [4, 5]]
flattened_list = []
for sub_list in nested_list:
    for item in sub_list:
        flattened_list.append(item)
print(flattened_list)

# alternate faster approach
merged_list = list(itertools.chain.from_iterable(nested_list))
print(merged_list)
