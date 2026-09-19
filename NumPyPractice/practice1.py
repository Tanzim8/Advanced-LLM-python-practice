import numpy as np 

grades = np.array([72, 87, 90, 67, 81])

print(grades.mean())
print(grades.max())
print(grades.min())

gradesDouble = grades*2

print("Doubling the grades using numPy", gradesDouble)

#practice with 2D array and using ndim, shape and size

collectedGrades = np.array([[78, 85, 91],
                            [68, 89, 97],
                            [88, 57, 78]
                        ])

print("Array dimension: ",collectedGrades.ndim)
print("Array shape: ",collectedGrades.shape)
print("Array size: ",collectedGrades.size)

differentDinmensionArray = np.array([[20, 45, 78, 88],
                                    [89, 65, 44, 91]
])

print("New Array dimension: ",differentDinmensionArray.ndim)
print("New Array shape: ",differentDinmensionArray.shape)
print("New Array size: ",differentDinmensionArray.size)

#indexing 1D array
print(grades[0])
print(grades[1])
print(grades[-1])

#indexing 2D arrays
#Format [row, column]
print(collectedGrades[0,0])
print(collectedGrades[1,2])

#getting an entire row

print(collectedGrades[0, :])


#getting an entire column
print(collectedGrades[:, 1])#means every row from column one

#slicing

print(grades[1:4])

#slicing for 2D
print(collectedGrades[0:2, 1:3])

#Math operations

print(grades+5)

#operation between arrays

a = np.array([40, 50, 60])
b = np.array([33, 21, 12])

print("result of adding 2 arrays: ",a+b)


#statistics using numpy

print(np.mean(grades))
print(np.median(grades))
print(np.std(grades))
print(np.var(grades))

print(np.min(grades))
print(np.max(grades))
print(np.sum(grades))

#2D array statistics

print(np.mean(collectedGrades))

#using axis to find average for each student
print(np.mean(collectedGrades, axis = 1))

#now average grade in each course
print(np.mean(collectedGrades, axis = 0))


#Boolean filtering

print(grades > 70)

#filtering dataset
print(grades[grades>70])

#changing values

scores = np.array([45, 65, 94, 33, 81])

scores[scores< 50] = 50

print(scores)

#reshaping arrays

numbers = np.array([1, 2, 3, 4, 5, 6])

print("The shape before reshape: ", numbers.shape)

matrix = numbers.reshape(2,3)

print("After reshape", matrix)

#Transposing

data = np.array([
    [1,2,3],
    [4,5,6]
])
print("Before transposing: ", data)
print("After transposing: ", data.T)

#special array

specialNumber = np.arange(1,13)
print("before aranging: ", specialNumber)
specialMatrix = specialNumber.reshape(3,4)
print("After aranging: ",specialMatrix)


#Random numbers

rng = np.random.default_rng()

randomNumbers = rng.integers(1,101, size= 10)

print(randomNumbers)

RandomGrades = rng.integers(50, 101, size=(20,5))
print(RandomGrades)

#matrix multiplication
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(np.matmul(A,B))
