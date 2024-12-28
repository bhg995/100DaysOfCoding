student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#print(max(student_scores))
#print(min(student_scores))
#print(sum(student_scores))

maximum = 0
for s in student_scores:
    if s > maximum:
        maximum = s
    #print(maximum)
print(maximum)
