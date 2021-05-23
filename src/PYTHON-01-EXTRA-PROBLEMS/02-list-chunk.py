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
