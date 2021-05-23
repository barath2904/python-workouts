k = 5
print(F"K value: {k}\n")

a = [5, 1, 2, 3, 10, 59, 15]
a.sort()
print(F"ascending sorted list: {a}")
# kth largest
if len(a) == k:
    print(a[0])
elif len(a) > k:
    print(a[(len(a)-k)])
    # K largest elements
    print(sorted(a[(len(a) - k):], reverse=True))
else:
    print("not applicable")

print("\n")

b = [5, 1, 2, 3, 10, 59, 15]
b.sort(reverse=True)
print(F"descending sorted list: {b}")
# kth smallest
if len(b) == k:
    print(b[0])
elif len(b) > k:
    print(b[(len(b)-k)])
    # K smallest elements
    print(sorted(b[(len(b) - k):], reverse=True))
else:
    print("not applicable")
