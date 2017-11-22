if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

count = 0
total = 0

for score in student_marks[query_name]:
    count += 1
    total += score

print "%.2f" % (total / count)
