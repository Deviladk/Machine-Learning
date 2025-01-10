stacked=pd.melt(users,id_vars='name',var_name='variable',value_name='value')
print(stacked)