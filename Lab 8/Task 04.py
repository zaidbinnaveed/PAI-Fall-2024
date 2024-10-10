import numpy as np

data = np.array([('Zaid', 5.9, 'A'), 
                 ('Waleed', 5.5, 'B'), 
                 ('Mustafa', 6.0, 'A'), 
                 ('Wajeeha', 5.7, 'B'),
                 ('Zumer', 5.8, 'A'),
                 ('Uzma', 5.6, 'C'),
                 ('Naveed', 5.9, 'B')],
                dtype=[('name', 'U10'), ('height', 'f4'), ('class', 'U1')])

sorted_data = np.sort(data, order=['class', 'height'])

print(sorted_data)
