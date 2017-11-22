def mutate_string(string, position, character):
    i = int(position)
    mutated_string = string[:i] + character + string[i +1:]
    return mutated_string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, i, c)
    print s_new
