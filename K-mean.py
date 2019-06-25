#KMEAN CLUSTERING with given number of CLUSTERS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#IMPORTING DATASET
dataset = pd.read_csv(r"C:\Users\imanm\Desktop\mark2\Churn_Modelling.csv")
x = dataset.iloc[:,[8,12]].values

#let the number of required clusters be 4
kmeans = KMeans(n_clusters= 4,random_state=1)
y = kmeans.fit_predict(x)
#visualisation
plt.scatter(x[y == 0,0],x[y == 0,1],s = 50, c='red',label='Cluster 1')
plt.scatter(x[y == 1,0],x[y == 1,1],s = 50, c='blue',label='Cluster 2')
plt.scatter(x[y == 2,0],x[y == 2,1],s = 50, c='yellow',label='Cluster 3')
plt.scatter(x[y == 3,0],x[y == 3,1],s = 50, c='green',label='Cluster 4')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1] ,s = 50, c='cyan',label='centroid')
plt.title('KMEAN CLUSTERING')
plt.xlabel('balance')
plt.ylabel('average salary')
plt.legend()
plt.show()

