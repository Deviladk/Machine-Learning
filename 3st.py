def Digital(nu):
    nu1=0
    while(nu>0):
        nu1=int(nu1+nu%10)
        nu=int(nu/10)
    
    if(nu1>9):
       nu1=Digital(nu1)
    
    return nu1
nu=int(input("Enter number "));
print(int(Digital(nu)));
