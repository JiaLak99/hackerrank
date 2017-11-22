A = set(raw_input().split())

truth = 'True'

for x in range (input()):
    B = set(raw_input().split())
    if len(B.intersection(A)) != len(B):
        truth = 'False' 

print truth
