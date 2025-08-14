import numpy as np

print("\n#1\n")
array = np.arange(10, 20)
print(array)
print(array.dtype)
total = array.sum()
print(total)
average = array.mean()
print(average)
minimum = array.min()
print(minimum)
maximum = array.max()
print(maximum)
    
assert total == 145, "Сума масиву повинна дорівнювати 145"
assert average == 14.5, "Середнє значення масиву повинно дорівнювати 14.5"
assert minimum == 10, "Мінімальне значення масиву повинно бути 10"
assert maximum == 19, "Максимальне значення масиву повинно бути 19"
    


print("\n#2\n")

array = np.arange(1, 1001, dtype=np.float64)
print(array.sum())
print(array.mean())
print(array.min())
print(array.max())


print("\n#3\n")

array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print("\nвсі елементи другого стовпця\n", array[: 1])
print("\nелементи з другого рядка\n", array[1 :])
print("\nзміна форми масиву на одномірний за допомогою flatten\n", array.flatten())

print("\n#4\n") 

array = np.arange(1, 500001, dtype=np.float64)
print(array.sum())
print(array.mean())
print(array.min())
print(array.max())

