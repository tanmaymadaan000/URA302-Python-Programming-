import numpy as np

# Question 1
arr1 = np.arange(5, 26)
arr2 = np.random.randint(10, 51, size=(3, 4))

# Question 2
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)

print(arr2.shape)
print(arr2.size)
print(arr2.dtype)

# Question 3
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

# Question 4
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3 * 5)

# Question 5
arr4 = np.arange(10, 26).reshape(4, 4)
print(arr4[1, :])
print(arr4[:, -1])
arr4[0, :] = 0
print(arr4)

# Question 6
arr5 = np.random.randint(20, 41, size=10)
print(arr5[arr5 > 30])

# Question 7
arr6 = np.arange(11, 23)
arr6_reshaped = arr6.reshape(3, 4)
print(arr6_reshaped)

# Question 8
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.matmul(A, B))
print(A.T)

# Question 9
arr7 = np.random.randint(10, 61, size=15)
print(np.mean(arr7))
print(np.median(arr7))
print(np.std(arr7))

# Question 10
A = np.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]])
print(np.linalg.det(A))
print(np.linalg.inv(A))
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)

# Question 11
positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
dist_first_last = np.linalg.norm(positions[-1] - positions[0])
print(dist_first_last)
step_distances = np.linalg.norm(np.diff(positions, axis=0), axis=1).sum()
print(step_distances)
