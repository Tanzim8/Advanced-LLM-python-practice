import numpy as np

grades = np.array([
    [78, 85, 92, 67],
    [88, 76, 81, 90],
    [55, 62, 70, 68],
    [95, 91, 89, 94],
    [72, 80, 77, 83]
])

print("Shape: ",np.shape(grades))
print("Student 3 grades: ", grades[2,])
print("Everyones grade in course 2: ", grades[:,1])
print("Everyones average: ",np.mean(grades))
print("Each students average: ", np.mean(grades, axis=1))
print("Each courses average: ", np.mean(grades, axis=0))
print("The highest score: ", np.max(grades))
print("The lowest score: ", np.min(grades))
print("Grades that are more than 85: ",np.sum(grades[grades>85]))
print("The count of grades that are more than 85: ",np.count_nonzero(grades>85))
print("Student 4's Max grade: ", np.max(grades[3]))
print("The average of course 3:", np.mean(grades[:,2]))
grades[grades<60] = 60
print("first 3 students and first 2 courses: ",grades[0:3,0:2])
print(grades[grades>=90])
