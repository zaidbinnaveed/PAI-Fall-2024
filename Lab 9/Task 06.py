import matplotlib.pyplot as plt

math_marks = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
science_marks = [80, 85, 77, 91, 86, 75, 93, 87, 83, 90]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='blue', label='Students')

plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Comparison of Mathematics and Science Marks')
plt.legend()
plt.show()
