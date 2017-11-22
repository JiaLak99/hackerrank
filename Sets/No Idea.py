trash = raw_input()
l1 = raw_input().split(' ')
s1, s2 = set(raw_input().split(' ')), set(raw_input().split(' '))

happiness = 0

for x in range (len(l1)):
    if l1[x] in s1:
        happiness += 1
    elif l1[x] in s2:
        happiness -= 1

print happiness
