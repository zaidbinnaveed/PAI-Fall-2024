import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
populations = [8419600, 3980400, 2716000, 2328000, 1680000, 
               1584200, 1547000, 1423800, 1343000, 1028000]

plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='skyblue')
plt.xlabel('Population')
plt.title('Population of Cities')
plt.show()
