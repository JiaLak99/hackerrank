def capitalize(string):
    words = string.split(' ')
    capitalized_list = []

    for word in words:
        if word:
            l = list(word)
            l[0] = l[0].upper()
            word = ''.join(l)
            capitalized_list.append(word)
        else:
            capitalized_list.append('')
            
    return ' '.join(capitalized_list)

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
