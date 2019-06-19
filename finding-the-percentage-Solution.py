def Average(Marks): 
    return sum(Marks) / len(Marks)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split(" ")
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
Marks = list(student_marks[query_name])

average = Average(Marks)
print("%0.2f" % (average))
