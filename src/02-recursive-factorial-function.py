# recursive function
# recursive function is a function that calls itself


def recursive_factorial(num):
    if num == 1:
        return num
    else:
        return num * recursive_factorial(num-1)

# Functionality explanation:
# factorial(n)                                # 1st call
# n * factorial(n-1)                          # 2nd call
# n * n-1 * factorial(n-2)                    # 3rd call
# n * n-1 * n-2 * factorial (n-3)             # 4th call
# ...............................             # till n calls
# recursive functions are clean & elegant, but recursive calls are expensive


def normal_factorial(num):
    if num == 1:
        return num
    else:
        result = 1
        for i in range(1, num):
            result = result * (i+1)
        return result


if __name__ == '__main__':
    x = int(input("Enter the number to find factorial for:"))
    print(recursive_factorial(x))
    print(normal_factorial(x))
