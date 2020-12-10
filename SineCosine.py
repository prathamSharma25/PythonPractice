import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-360,360,45)*np.pi/180

plt.subplot()
sin_=plt.plot(x, np.sin(x),label="Sine Curve")
cos_=plt.plot(x,np.cos(x),label="Cos Curve")
#_tan=plt.plot(x,np.tan(x),label="Tan Curve")
plt.legend(['sin','cos'])

plt.show()
