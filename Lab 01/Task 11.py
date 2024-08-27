grades = {}
grades['math'] = int(input("Enter marks for Math: "))
grades['science'] = int(input("Enter marks for Science: "))
grades['english'] = int(input("Enter marks for English: "))
total = sum(grades.values())
average = total / len(grades)
percentage = (total / 300) * 100
print("Average:", average)
print("Percentage:", percentage)
