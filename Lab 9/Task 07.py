import matplotlib.pyplot as plt

years = [1923, 1933, 1943, 1953, 1963, 1973, 1983, 1993, 2003, 2013, 2023]
sea_levels = [1.2, 1.5, 1.7, 1.8, 2.0, 2.3, 2.5, 2.7, 3.0, 3.3, 3.5]

plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue')

plt.xlabel('Year')
plt.ylabel('Sea Level (in meters)')
plt.title('Sea Level Rise Over the Past 100 Years')
plt.show()
