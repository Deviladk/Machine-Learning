n=int(input("number "))
lis=[]
x=1
for i in range(1,n+1):
    sum=0
    for j in range(5):
       sum=sum+x
       if(j<4):
        lis.append(x)
        x+=1
       else:
        lis.append(sum);
print(lis)