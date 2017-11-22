import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase

    for i in range (size - 1, 0, -1):
        row = ['-'] * (size * 2 - 1)
        for j in range (size - i):
            row[size - j - 1] = alphabet[i + j]
            row[size + j - 1] = alphabet[i + j]
        print '-'.join(row)

    for i in range (size):
        row = ['-'] * (size * 2 - 1)
        for j in range (size - i):
            row[size - j - 1] = alphabet[i + j]
            row[size + j - 1] = alphabet[i + j]
        print '-'.join(row)

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
