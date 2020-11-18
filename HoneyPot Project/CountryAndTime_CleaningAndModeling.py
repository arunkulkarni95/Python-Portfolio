# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:02:44 2020

@author: Arun
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
#import raw data
#reorganize/rename columns
df = pd.read_csv('AttacksByCountryAndTime.csv')

df['Time'] = df['Time']
df['Time'] = df['Time'].map(lambda x : x / 1000)
#df['Time'] = pd.to_datetime(df['Time'],unit='s')

#print(df)

_ = plt.figure(figsize=(12,6.75))
_ = plt.style.use('ggplot')
_ = sns.scatterplot(x='Time',y='NumberOfAttacks',data=df,hue='Country',legend=False)
_ = plt.xlabel('Time')
_ = plt.ylabel('Number of Attacks')
_ = plt.title('Honeypot Attacks by Country and Time')
plt.show()

X_train, X_test, y_train, y_test = \
    train_test_split(df[['Time','NumberOfAttacks']],\
                     df['Country'],test_size=0.3,\
                         random_state=21,stratify=df['Country'])

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)
print('\n')
print(y_pred)
score = knn.score(X_test,y_test)
print('\n')
print(score)
print('\n')

rho1 = np.corrcoef(df['Time'],df['NumberOfAttacks'],rowvar=False)
print(rho1)
print('\n')
