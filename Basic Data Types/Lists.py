if __name__ == '__main__':
    N = int(raw_input())
arr = []
for x in range(N):
    listOfCommands = raw_input().split()
    command = listOfCommands[0]
    arguments = listOfCommands[1:]
    if (command != 'print'):
        command += "("+ ",".join(arguments) +")"
        eval("arr." + command)
    else:
        print arr
