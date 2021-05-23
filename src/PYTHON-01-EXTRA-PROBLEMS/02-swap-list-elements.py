# swap first & last elements
input_list = [1, 2, 3, 5]
# list unpacking
start, *middle, end = input_list
out_list = [end, *middle, start]
print(out_list)

# alternate approach
# this can work for swap of any 2 positions
ip_list = [1, 2, 3, 5]
ip_list[0], ip_list[-1] = ip_list[-1], ip_list[0]
print(ip_list)