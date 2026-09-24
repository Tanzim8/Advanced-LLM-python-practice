import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("ai_experiments.csv")

plt.hist(data["accuracy"])
plt.title("Distribution of Model Accuracy")
plt.xlabel("Accuracy")
plt.ylabel("Frequency")

plt.savefig("Model_accuracy.png")

plt.show()


# students = ["Tanzim", " Alex", "Maria", "Hasan"]
# grades = [82, 91, 87, 85]
# plt.bar(students, grades)
# plt.title("Student Grades")
# plt.xlabel("Student")
# plt.ylabel("Grade")
# plt.savefig("student_grades.png")
# plt.show()