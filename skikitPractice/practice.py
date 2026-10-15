import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "hours_studied": [1,2,3,4,5,6,7,8,9,10],
    "exam_score": [42, 50, 55, 62, 68, 73, 79, 85, 91, 96]
})

X = data[["hours_studied"]]
y = data[["exam_score"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.2, random_state= 42
)

print("Training features: ")
print(X_train)

print("Testing fesatures: ")
print(X_test)

#Creates the model
model = LinearRegression()

#Trains using the training examples
model.fit(X_train, y_train)

#Makes predoctions
predictions = model.predict(X_test)

print("Predicted scores: ", predictions)
print("Actual scores: ", y_test.values)


#MAE = Mean Absolute Error
mae = mean_absolute_error(y_test, predictions)

print("MAE: ", mae)

#Coefficient
print("Coefficient: ", model.coef_)
#intercept
print("Intercept: ", model.intercept_)

#Linear Regression y = coefficient*x + intercept

#For 6 hours studied the linear regression would be 
res = model.coef_*6 + model.intercept_
print("Linear regression for 6 hours: ", res)

#for 12 hours: Reults in Extrapolation(prediction out of range) 
resTwelve = model.coef_*12 + model.intercept_
print("For twelve hours: ", resTwelve)
