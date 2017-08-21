from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
array = []
for i in range (1, n + 1):
    array.append(i)
print (*array, sep = '')
