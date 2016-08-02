import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fr = pd.read_csv("TVlife.txt", header=0)

fr['ones'] = 1

A = fr.as_matrix(['ones','x'])
b = fr.as_matrix(['y'])

Atransp = np.transpose(A)
AtranspA = np.dot(Atransp, A)
AtranspA_inv = np.linalg.inv(AtranspA)
AtranspA_invAtransp = np.dot(AtranspA_inv, Atransp)
xhat = np.dot(AtranspA_invAtransp, b) #[C, D]

print "C (intercept) = %2.3f" % xhat[0]
print "D (slope) = %1.3f" % xhat[1]

e = b - np.dot(A, xhat)
enorm = np.linalg.norm(b-np.dot(A, xhat))

print "e (error) = %1.3f" % enorm

fig = plt.figure()
plt.plot(fr.x, fr.y, "b+")
plt.plot(fr.x, xhat[0] + xhat[1]*fr.x, color="black")
plt.title("Life expectancy per televisions per thousand people", fontsize=16)
plt.xlabel("Televisions per thousand people", fontsize=16)
plt.ylabel("Life expectancy (years)", fontsize=16)
plt.text(400, 60, "y = %2.3f + %1.3f*x" % (xhat[0], xhat[1]), fontsize=16)

fig.savefig('TV_reg.png', format="png")
plt.show()
