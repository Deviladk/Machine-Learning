def troide(x):
    y=int(x%10)
    x=int(x/10)
    z=int(x%10)
    j=int(x/10)
    if(y==z or y==j or z==j):
       return False
    return True



for x in range(102,439):
 if(troide(x)):
    z=2*x
    if(troide(z)):
       k=3*x
       if(troide(k)):
          print(x,x*2,x*3)
         
