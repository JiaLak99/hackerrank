def print_formatted(number):
    number += 1
    width = len('{:b}'.format(n))

    for i in range(1, number):
        print str.rjust(str(i), width),\
        str.rjust('{:o}'.format(i), width),\
        str.rjust('{:X}'.format(i), width),\
        str.rjust('{:b}'.format(i), width)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
