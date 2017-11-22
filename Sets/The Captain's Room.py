trash = input()
s = raw_input().split()
s1 = set()
s2 = set()

for entry in s:
    if entry not in s1:
        s1.add(entry)
    else:
        s2.add(entry)

print s1.difference(s2).pop()
