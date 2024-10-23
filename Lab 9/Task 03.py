import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 
           'Rocky Road', 'Pistachio', 'Neapolitan']
scoops_sold = [250, 300, 150, 200, 100, 180, 120, 220]

plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title('Ice Cream Sales Distribution')
plt.show()
