


import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#Library - A collection of packages.
#Package - A collection of predetermined codes.
#Module - Lines of codes.

# Class - Blueprint
# Object - an instance of class
# Methods - A behaviour of class

# Pip install scikit-learn

# 

""" x = pd.read_csv('QuizScore - QuizScore.csv')#COMMA SEPARATED VALUE
x.fillna('Mary Jovily', inplace=True)

print(x)"""

my_data = pd.read_csv('QuizScore - QuizScore.csv')

X = my_data.drop(columns=['Sex'])
y = my_data['Sex']

model = DecisionTreeClassifier()
model.fit(X,y)

result = model.predict([ [] ])

print(result)

