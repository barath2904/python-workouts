# looping
def mul_table(num):
    # range function returns from x to y-1 in range(x,y)
    # range function returns from 0 to n-1 in range(n)
    for i in range(1, 11):
        print(str(num) + ' x ' + str(i) + ' = ' + str(num*i))


if __name__ == '__main__':
    n = int(input("enter the number to build multiplication table for:"))
    mul_table(n)
