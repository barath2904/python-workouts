# looping + String operation
def index_split(line_content):
    even_string = ''
    odd_string = ''
    for index in range(len(line_content)):
        if index % 2 == 0:
            even_string += line_content[index]
        else:
            odd_string += line_content[index]
    print(even_string + "  " + odd_string)


if __name__ == '__main__':
    n = int(input("enter the number of lines:"))

    line_list = []
    for i in range(n):
        line = input("enter line content:")
        line_list.append(line)

    for line_string in line_list:
        index_split(line_string)
