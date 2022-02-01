from linear_model import LinearRegression

#datasets
X = np.array([1,2,3,4,5,6,7,8,9], dtype='float64')
y = np.array([4.5,7.5,10.5,13.5,16.5,19.5,22.5,25.5,28.5], dtype='float64')

#create model object
model = LinearRegression()

model2 = LinearRegression()

#training
model.fit(X,y)

#regression parameters
model.coef_
model.intercept_

#predicting on single data
model.predict(5)

