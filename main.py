import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def NormalCDF(value, N):
  
  sum=0
  
  for k in range(N+1):
    term = (-1)**k*value**(2*k+1)/(2**k*math.factorial(k)*(2*k+1))
    sum+=term
    
  return 0.5+1/(2*math.pi)**(1/2)*sum

def ProbXgreaterthanY(meanX, varX, meanY, varY, N):
  
  new_mean = meanX-meanY
  new_var = varX+varY
  
  value = -new_mean/math.sqrt(new_var)
  probability = 1 - NormalCDF(value, N)

  sigmaX = math.sqrt(varX)
  sigmaY = math.sqrt(varY)
  
  x = np.linspace(min(meanX - 3*sigmaX, meanY - 3*sigmaY), max(meanX + 3*sigmaX, meanY + 3*sigmaY), 100)
  
  plt.plot(x, norm.pdf(x, meanX, sigmaX), label="Stock X ("+"$\mu$="+str(meanX)+" $\sigma=$"+str(round(sigmaX,2))+")")
  plt.plot(x, norm.pdf(x, meanY, sigmaY), label="Stock Y ("+"$\mu$="+str(meanY)+" $\sigma=$"+str(round(sigmaY,2))+")")

  plt.xlabel("Annual Return (%)")
  plt.title("Probability Density Functions of Returns")

  return str(round(probability*100, 2))+'%', plt.legend()
