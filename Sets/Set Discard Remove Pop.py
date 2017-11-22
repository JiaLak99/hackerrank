n = input()
s = set(map(int, raw_input().split())) 
N = input()

for x in range(N):
    command = raw_input().split(' ')
    if 'pop' == command[0]:
        s.pop()
    elif 'remove' == command[0]:
        s.remove(int(command[1]))
    elif 'discard' == command[0]:
        s.discard(int(command[1]))
    
print(sum(s))
