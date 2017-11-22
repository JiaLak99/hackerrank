def swap_case(s):
    swapped_string = s.swapcase()
    return swapped_string

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
