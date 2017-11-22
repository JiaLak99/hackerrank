s1, s2 = [set(raw_input().split(' ')) for x in range (4)][1::2]
print len(s1.difference(s2))
