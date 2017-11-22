import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string = raw_input()
    max_width = int(raw_input())
    result = wrap(string, max_width)
    print result
