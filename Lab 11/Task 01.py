#name:  Zaid Bin Naveed
#date: 13 november 2024
#lab: 11
#task: 01

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#step 1: Load the dataset
# Using a typical heart disease dataset (for demonstration, using one from UCI repository).
# Replace 'path_to_heart_disease_data.csv' with actual data file path or dataset.
data = pd.read_csv("heart.csv")

#step 2: Preprocess the data
#assume the target variable is in a column named 'target'
X = data.drop(columns=['target'])
y = data['target']

#standardize features for better KNN performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#step 3: train and evaluate KNN classifier across multiple k values
k_values = range(1, 251)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

#find the best and worst performing k values
max_accuracy = max(accuracies)
min_accuracy = min(accuracies)
best_k = [k for k, acc in zip(k_values, accuracies) if acc == max_accuracy]
worst_k = [k for k, acc in zip(k_values, accuracies) if acc == min_accuracy]

#step 4: plot accuracy vs. number of neighbors
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, color='blue', linestyle='-', marker='o')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy for Different Numbers of Neighbors')
plt.grid(True)
plt.show()

#print the results
print(f"Highest Accuracy: {max_accuracy * 100:.2f}% at k = {best_k}")
print(f"Lowest Accuracy: {min_accuracy * 100:.2f}% at k = {worst_k}")
