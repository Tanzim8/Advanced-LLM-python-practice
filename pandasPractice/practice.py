import pandas as pd

data = {
    "Student" : ["Tanzim", "Alex", "Jhon", "Maria"],
    "Python" : [78, 91, 76, 74],
    "Math" : [93, 89, 98, 82],
    "English": [81, 90, 93, 89]
}

#DataFrame = multiple colums / table
students = pd.DataFrame(data)
print(students)

#Series = one column
print(students["Python"])

#Selecting multiple columns
print(students[["Python", "Math"]])

#The average of the python course grades
print(students["Python"].mean())

#The max
print(students["Python"].max())

#The lowest
print(students["Python"].min())

#The sum of all python course grades
print(students["Python"].sum())

#The describe tool -- Gives a statistical summary of all

print(students.describe())


#Filtering
#only printing grades more than 80
print(students[students["Python"] > 80])

print(students[
    (students["Python"] > 80)&
    (students["Math"]>80)
])

#loc and iloc 

#loc = position

#This gets the first row
print(students.iloc[0])
#This gets the 3rd row
print(students.iloc[2])

#This gets the first 3 students
print(students.iloc[0:3])

#Adding new column
students["Average"]=students[
    ["Python", "Math", "English"]
].mean(axis=1)
print(students)

#Adding new row
students.loc[len(students)]= ["Hasan", 80, 85, 90, 85]

print(students)
print(students.columns)
print(len(students.columns))