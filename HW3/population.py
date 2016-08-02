import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fr = pd.read_csv("population.txt", header=0)

fr['ones'] = 1

A = fr.as_matrix(['ones','x'])
b = fr.as_matrix(['y'])

Atransp = np.transpose(A)
AtranspA = np.dot(Atransp, A)
AtranspA_inv = np.linalg.inv(AtranspA)
AtranspA_invAtransp = np.dot(AtranspA_inv, Atransp)
xhat = np.dot(AtranspA_invAtransp, b) #[C, D]

print "C (intercept) = %1.3e" % xhat[0]
print "D (slope) = %1.3e" % xhat[1]

fig = plt.figure()
plt.plot(fr.x, fr.y, "b+")
plt.plot(fr.x, xhat[0] + xhat[1]*fr.x, color="black")
plt.title("National population per year", fontsize=16)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Population", fontsize=16)
plt.text(1920, 2.6e8, "y = %1.3e + %1.3e*x" % (xhat[0], xhat[1]), fontsize=16)

fig.savefig('pop_reg.png', format="png")
plt.show()
