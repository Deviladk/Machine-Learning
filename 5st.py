import numpy as np
# list3=[range(1,6),range(6,11)]
# print(list3,type(list3))
# arr2=np.array(list3)
# print(arr2,type(arr2))

#Finding out the cartesion distance between two points in n-dimensional space
# pt1(x1,y1) and pt2(x2,y2)=>cart_dis=((x1-y1)^2)+(x2-y2)^2)^0.5
pt1=np.array([100,200,202,303,404])
pt2=np.array([340,506,607,325,177])
cart_dis =0
for i in range(len(pt1)):
    cart_dis+=(pt1[i]-pt2[i])**2
print(cart_dis**0.5)
print(np.sqrt(np.sum(np.power(np.subtract(pt1,pt2),2))))