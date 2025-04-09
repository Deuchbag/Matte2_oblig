import numpy as np

x = 1.5


for i in range(1,20):
    h = 1*10**(-i)
    f_est = ((np.exp(x-2*h) - 8*np.exp(x-h) + 8*np.exp(x+h) - np.exp(x+2*h))/(12*h))
    print(f_est, i)

#her igjen så ser vi at på desimal 15 så funker ikke tilnærmingen lenger.