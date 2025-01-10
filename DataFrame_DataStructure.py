import numpy as np
import pandas as pd
user_data=[['alice',19,'F','sudent'],['john',26,'M','student']]
user_columns=['name','age','gender','job']
user1=pd.DataFrame(data=user_data,columns=user_columns)
# print(user1)
user1.columns=user_columns
# user1

user_data=dict(name=['eric','paul'],age=[22,58],gender=['M','F'],job=['student','manager'])
print(user_data)
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
print(users_outer)

print(users_outer.any())
print(users_outer.all())