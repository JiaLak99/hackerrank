grades = []
for _ in range(int(raw_input())):
    grades.append([raw_input(), float(raw_input())])

sortGrades = sorted(set([b for a, b in grades]))[1]
print '\n'.join(sorted([a for a, b in grades if b == sortGrades]))
