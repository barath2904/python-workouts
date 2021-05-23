# 2D array
# prints BIG
image = [
 [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1,  0, 0, 1, 0, 0,  1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 0, 1, 1, 1],
 [1, 0, 0, 0, 1,  0, 0, 1, 0, 0,  1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1,  0, 0, 1, 0, 0,  1, 1, 1, 1, 1]
]

for pixel_row in image:
    for pixel in pixel_row:
        if pixel is 1:
            fill = "*"
        else:
            fill = " "
        print(fill, end=' ')
    print('')
