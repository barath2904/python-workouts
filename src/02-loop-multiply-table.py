import sys


# looping
def mul_table(num):
    # range function returns from x to y-1 in range(x,y)
    # range function returns from 0 to n-1 in range(n)
    for i in range(1, 16):
        print(str(num) + ' x ' + str(i) + ' = ' + str(num*i))


if __name__ == '__main__':
    try:
        n = int(input("enter the number to build multiplication table for:"))
        mul_table(n)
    except ValueError as e:
        print(F"Enter valid value to run multiplication program.\n{e}")
        sys.exit(1)
