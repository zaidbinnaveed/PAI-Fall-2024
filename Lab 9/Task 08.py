x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

plt.plot(x, y1, color='pink', marker='o', label='Y1 Data')
plt.plot(x, y2, color='gray', marker='o', label='Y2 Data')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(loc='lower right')
plt.show()
