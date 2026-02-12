def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1} out of 100: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

grade = calculate_grade(average)

print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
