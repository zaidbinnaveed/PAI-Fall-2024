import matplotlib.pyplot as plt

genders = ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female']
gender_counts = {'Male': 0, 'Female': 0}

for gender in genders:
    gender_counts[gender] += 1

labels = gender_counts.keys()
sizes = gender_counts.values()
colors = ['skyblue', 'pink']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Gender Distribution of Students")
plt.show()
