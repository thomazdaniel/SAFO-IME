import numpy as np
from scipy.optimize import minimize_scalar
f = lambda x : 5* np.cos(2*x) - 2*x*np.sin(2*x)
res = minimize_scalar (f , bounds =(1 ,2) , method = 'bounded')
print (res.x , f(res.x))