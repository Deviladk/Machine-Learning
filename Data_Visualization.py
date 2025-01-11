import numpy as np
import matplotlib.pyplot as plt


# x=np.linspace(0,10,50)
# sinus=np.sin(x)
# plt.plot(x,sinus,"--")
# plt.show()


#  //////////    Rapid Multiplot
x=np.linspace(0,10,50)
sinus=np.sin(x)
cosinus=np.cos(x)
# plt.plot(x,sinus,'b',x,cosinus,'-r',x,sinus,'ob',x,cosinus,'or')
# plt.xlabel("Plotting x-values")
# plt.ylabel("Plotting Sin(x) or Cos(x)")
# plt.title("Plotting sin(x) and Cos(x) against x value...")
# plt.show()



plt.plot(x,sinus,label='sinus',color='blue',linestyle='--')
plt.plot(x,cosinus,label='sinus',color='blue',linestyle='--')
plt.xlabel("Plotting x-values")
plt.ylabel("Plotting Sin(x) or Cos(x)")
plt.title("Plotting sin(x) and Cos(x) against x value...")
plt.show()