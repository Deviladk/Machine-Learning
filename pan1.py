import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# s=pd.Series()
# print(s,type(s))


# arr_data=np.array([100,200,400,500,300])
# print(arr_data,type(arr_data))
# s=pd.Series(data=arr_data,copy=False)
# print(s)

# s=pd.Series(arr_data)
# print(s)
# print(s[0],s[1])
# print(s[0:3])


# arr1=np.array([100,200,300,400,500])
# print(arr1,type(arr1))
# s=pd.Series(data=arr1,copy=False)
# print(s,type(s))
# arr1[0]=111
# s[4]=555
# print("After update...")
# print(arr1)
# print(s)


# arr1=np.array([100,200,300,400,500])
# print(arr1,type(arr1))
# s=pd.Series(data=arr1,copy=True)
# print(s,type(s))
# arr1[0]=111
# s[4]=555
# print("After update...")
# print(arr1)
# print(s)

# arr_data=np.array(["a","b","c","p"])
# print(arr_data,len(arr_data))
# s=pd.Series(data=arr_data)
# print(s)
# print(s[0],s[1])


# arr_data=np.array(["a","b","c","p"])
# print(arr_data,len(arr_data))
# s=pd.Series(data=arr_data,index=[100,101,102,103])
# print(s)


# indexing non-numeric
# arr_data=np.array(["a","b","c","p"])
# print(arr_data,len(arr_data))
# s=pd.Series(data=arr_data,index=["x","y","z","xy"])
# print(s)



#creating a series from a dictionary
# dict_data={'a':104,'b':205,'c':306,'d':607}
# print(dict_data)
# s=pd.Series(data=dict_data)
# print(s)

#Crearing Series from a constant
# s=pd.Series(data=50,index=[0,1,2,3,4,5,6])
# print(s)
# s=pd.Series(data=50,index=[0,1,2,3,0,0,1,2]);
# print(s)



#Creating series from a list
# s=pd.Series(data=[11,33,22,55,44])
# print(s)
# s=pd.Series(data=[11,33,22,55,44],index=['red','green','blue','magenta','cyan'])
# print(s)


