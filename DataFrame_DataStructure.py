import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
user_data=[['alice',19,'F','sudent'],['john',26,'M','student']]
user_columns=['name','age','gender','job']
user1=pd.DataFrame(data=user_data,columns=user_columns)
# print(user1)
user1.columns=user_columns
# user1

user_data=dict(name=['eric','paul'],age=[22,58],gender=['M','F'],job=['student','manager'])
# print(user_data)
user2=pd.DataFrame(data=user_data)
# user2

user_data={'name':['peter','julie'],'age':[33,44],'gender':['M','F'],'job':['engineer','scientist']}
user3=pd.DataFrame(data=user_data)
# print(user3)



#  ////  COncatenating DataFrames
users=pd.concat([user1,user2,user3],ignore_index=True)
users1=pd.DataFrame(users)
# print(users1)


dict_data=dict(name=['alice','john','eric','julie','rita'],height=[165,168,170,180,167])
user4=pd.DataFrame(data=dict_data)
# print(user4)


#inner join
users_inner=pd.merge(users,user4,on='name',how='inner')
# print(users_inner)



#////outer join
users_outer=pd.merge(users,user4,on='name',how='outer')
# print(users_outer)


#//left outer join
users_left_outer=pd.merge(users,user4,on='name',how='left')
# print(users_left_outer)

#///right outer join
users_right_outer=pd.merge(users,user4,on='name',how='right')
# print(users_right_outer)


#Information 
# users.head(3)

# print(users.tail(3))
# print(users_outer)

# print(users_outer.any())
# print(users_outer.all())
#print(users)

# print(users.age)
# print(type(users.age))

# print(users[['job','name']])

# mycols=['job','name']
# print(users[mycols])



# bool_series=users.job=='manager'
# print(bool_series)
# print(bool_series)

# bool_series_age=(users.job=='student') & (users.age>=25) |(users.job=='manager')
# print(users[bool_series_age][['name','gender']])

# print(users.iloc[3])
# print(users.loc[3])
# print(users.index)

# print(users.iloc[4][3],users.iloc[4]['job'],users.loc[4][3],users.loc[4]['job'])
# print(users.iloc[4,3],users.iloc[4]['job'],users.loc[4][3],users.loc[4,'job'])


# df=users.copy()
# print(df)
# for row_index in range(df.shape[0]):
#     current_row=df.iloc[row_index]
#     current_row.age+=100
#     df.iloc[row_index]=current_row
# print(df)


# df=users.copy()
# print(df.age.sort_values())


# df.sort_values(by='age',ascending=False,inplace=True)
# df.index=range(df.shape[0])
# print(df)


#/////////    Pivot and Unpivot
#     wide Format---Unpivot----> Long Format(Stacked Format)
#     Long format(Stack Format)------Unpivot---->Wide Format

df=users.copy()
# print(df)
stacked=pd.melt(users,id_vars='name',var_name='variable',value_name='value')
# print(stacked)



# unstacked=stacked.pivot(index='name',columns='variable',values='value')
# unstacked.reset_index(inplace=True)
# unstacked.columns.name=''
# print(unstacked)



# //////////         Quality Control:Duplication Data


#dublication
# df=users.copy()
# df=pd.concat([df,df[df.index==0]])
# df=pd.concat([df,df[df.index==2]])
# df=pd.concat([df,df[df.index==4]])
# df.sort_values(by='name',inplace=True)
# df.index=range(df.shape[0])
# print(df)

#delete duplication
# df=df[~df.duplicated()]
# print(df)


#df=users_left_outer.copy()
# print(df)
# df.info()
# print(df.height.isnull())
#print("Number of Null enterieis is",df.height.isnull().sum())
#print(df.isnull().sum())
#print(df.notnull().sum())


#   ////////////////       Deleting entire row containing Nan values


# df=users_left_outer.copy()
# print(df)
# df.dropna(inplace=True)
# print(df)
# mean_height=df.height.mean()
# print(mean_height)
# df.fillna(mean_height,inplace=True)
# print(df)


#//////////////////   forward fill
# df=users_left_outer.copy()
# df.sort_values(by='age',inplace=True)
# df.index=range(df.shape[0])
# print(df)
# df.fillna(method='pad',inplace=True)
# print(df)

#/////////////////   backword fill
# df=users_left_outer.copy()
# df.sort_values(by='age',inplace=True)
# df.index=range(df.shape[0])
# print(df)
# df.fillna(method='bfill',inplace=True)
# print(df)


#////                    Group by

df=users.copy()
# for group,data_frame in df.groupby('job'):
#     print(type(group),type(data_frame))
#     print("Group name:",group)
#     print(data_frame)
grouped_df=df.groupby('job').agg({'age':['sum','mean','max','min'],'gender':'count'})
print(grouped_df)    

grouped_df=df.groupby('gender').agg({'age':['sum','mean','max','min'],'gender':'count'})
print(grouped_df) 














