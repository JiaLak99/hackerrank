s1, s2 = [set(raw_input().split(' ')) for x in range (4)][1::2]

s3 = s1.difference(s2)
s4 = s2.difference(s1)
s4.update(s3)

print '\n'.join(sorted(s4, key = int))
