import matplotlib.pyplot as plt
import numpy as np

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack',
            'Kathy', 'Liam', 'Mona', 'Nina', 'Owen', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tina']

heights = [150, 160, 165, 170, 155, 180, 175, 158, 162, 169,
           172, 168, 177, 159, 161, 165, 173, 157, 166, 164]

colors = plt.cm.viridis(np.linspace(0, 1, len(students)))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(students, heights, color=colors)
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.title('Bar Chart of Student Heights')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.pie(heights, labels=students, colors=colors, autopct='%1.1f%%')
plt.title('Pie Chart of Student Heights')

plt.tight_layout()
plt.show()
