import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
import numpy as np
import warnings



'''
    cough
    fever
    sore throat
    shortness of breath
    head ache
    gender
    above 60?

    
    covid result
'''


df=pd.read_csv('out.csv')

warnings.filterwarnings("ignore")


df_x=df.drop(df.columns[7],axis=1)
y=df.drop(df.columns[0:7],axis=1)
y=y.values.tolist()

scaler=StandardScaler()

df_x=scaler.fit_transform(df_x)
df_x=pd.DataFrame(df_x)

gnb=GaussianNB()
test=eval(input()) # input of the form (l,m,n,o,p,q,r)
test=np.asarray(test).reshape(1,7)
y_pred=gnb.fit(df_x,y).predict_proba(test)

print("Probability of Covid is %.2f percent" %(y_pred[0][0]*100))
