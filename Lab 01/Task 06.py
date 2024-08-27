scores = {}
scores['Physics'] = int(input("Enter marks for Physics: "))
scores['Chemistry'] = int(input("Enter marks for Chemistry: "))
scores['Maths'] = int(input("Enter marks for Maths: "))
mean = sum(scores.values()) / len(scores)
top_subject = max(scores, key=scores.get)
print("Average marks:", mean)
print("Highest marks in:", top_subject)
