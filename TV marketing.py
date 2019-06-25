#1) importing the modules required
import pandas as pd
import numpy as np
import seaborn as sns
#2)Setting up a dataframe
advertising = pd.read_csv(r'C:\Users\imanm\Desktop\Supervised_learning\Regression\Linear_Regreesion\tvmarketing.csv') #add the path for your csv file
sns.pairplot(advertising,x_vars='TV',y_vars= 'Sales',size = 6.7,kind='scatter')
x = advertising['TV']
y = advertising['Sales']
#3)importing a suitable model and assigning x & y values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7 , random_state=100)
x_train = x_train[:, np.newaxis]
x_test = x_test[:, np.newaxis]
print(x_train.ndim)
print(y_train.ndim)
#4)Performing Linear Regression
from sklearn.linear_model import LinearRegression
lr =LinearRegression()
lr.fit(x_train,y_train)
#5)Prediction
y_prediction = lr.predict(x_test)
print(lr.predict([[12]]))

