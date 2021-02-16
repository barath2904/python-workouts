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
