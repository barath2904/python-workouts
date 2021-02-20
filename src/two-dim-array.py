# 2D array
# image = [
#  [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 1,  0, 0, 1, 0, 0,  1, 0, 0, 0, 0],
#  [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 0, 1, 1, 1],
#  [1, 0, 0, 0, 1,  0, 0, 1, 0, 0,  1, 0, 0, 0, 1],
#  [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 1, 1, 1, 1]
# ]
#
# for pixel_row in image:
#     for pixel in pixel_row:
#         if pixel is 1:
#             fill = "#"
#         else:
#             fill = " "
#         print(fill, end=' ')
#     print('')


a = [5, 1, 2, 3, 10, 59, 15]
a.sort()
print(a)
k = 5
# kth largest
if len(a) == k:
    print(a[0])
elif len(a) > k:
    print(a[(len(a)-k)])
    # K largest elements
    print(sorted(a[(len(a) - k):], reverse=True))
else:
    print("not applicable")

# chunk the list based on n value
l = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
nl= []
if n != 0:
    for i in range(0, len(l), n):
        print(i)
        nl.append(l[i: i+n])
    print(nl)
else:
    print("not applicable")