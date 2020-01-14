import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib

#%matplotlib inline

#Download data from
#https://github.com/rstudio/keras-customer-churn/blob/master/data/WA_Fn-UseC_-Telco-Customer-Churn.csv

#df = pd.read_csv('telco.csv')
df = pd.read_csv('https://raw.githubusercontent.com/rstudio/keras-customer-churn/master/data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
