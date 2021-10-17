#load the data
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression
from sklearn.preprocessing import OneHotEncoder

out=pd.read_csv('out.tsv',sep='\t')
#next step
#need to create a subset based on case id
X=out[['Variant','Pizza Type','Pizza Size','Weekday','Daytime','Customer_Location','Customer_Type']]
X = pd.get_dummies(data=X,columns=['Variant','Pizza Type','Pizza Size','Weekday','Daytime','Customer_Location','Customer_Type'])
features=X.columns

#enc = OneHotEncoder(handle_unknown='ignore') #https://stackoverflow.com/questions/34007308/linear-regression-analysis-with-string-categorical-features-variables
#enc.fit(X)
#X=enc.transform(X).toarray()

y = np.array(out[['Revenue']])


#setup the model: Elastic net regression
X, y = make_regression(n_features=X.shape[1], random_state=103)
regr = ElasticNet(random_state=103)
regr.fit(X, y)



#interpret result
print(features)
print(regr.coef_.round(1))
print(regr.intercept_.round(1))
