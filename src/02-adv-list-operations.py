import itertools


def rec_flatten(nested_list_elements):
    # works for any kind of nested list
    result = []
    for list_element in nested_list_elements:
        if isinstance(list_element, list):
            result += rec_flatten(list_element)
        else:
            result.append(list_element)
    return result


nested_ip_list = [1, 2, [3, 4], [5, [6, [7]]]]
print(rec_flatten(nested_ip_list))

# --------------------------------------------------------------------------------------------------------------------

# works only for list of list
list_of_list = [[1, 2], [3, 4]]
merged_list = list(itertools.chain.from_iterable(list_of_list))
print(merged_list)

# alternate approaches for 2D list
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
# --------------------------------------------------------------------------------------------------------------------
# swap first & last elements
input_list = [1, 2, 3, 5]
start, *middle, end = input_list
out_list = [end, *middle, start]
print(out_list)

# alternate approach
# this can work for swap of any 2 positions
ip_list = [1, 2, 3, 5]
ip_list[0], ip_list[-1] = ip_list[-1], ip_list[0]
print(ip_list)
# --------------------------------------------------------------------------------------------------------------------
