def merge_the_tools(string, k):

    for i in range (len(string) / k):
        temp_string = ''

        for character in string[i * k: i * k + k]:            
            if character not in temp_string:
                    temp_string += character
                    
        print temp_string

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
