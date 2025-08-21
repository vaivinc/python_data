import numpy as np

print("\n#1\n")
array = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

array3 = np.hstack((array, array2))

print(array)
print(array2)
print(array3)


print("\n#2\n")

array = np.array([12, -5, 7, 9, -3, 15])

array2 = np.append(array, 10)

print(array)
print(array2)


print("\n#3\n")

array = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])

array2 = np.delete(array, 1, axis=0)

print("\nПерший:\n")
print(array)
print("\nДругий:\n")
print(array2)