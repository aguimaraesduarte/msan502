import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fr = pd.read_csv("nba.txt", header=0)

fr['ones'] = 1

A = fr.as_matrix(['ones','x'])
b = fr.as_matrix(['y'])

Atransp = np.transpose(A)
AtranspA = np.dot(Atransp, A)
AtranspA_inv = np.linalg.inv(AtranspA)
AtranspA_invAtransp = np.dot(AtranspA_inv, Atransp)
xhat = np.dot(AtranspA_invAtransp, b) #[C, D]

print "C (intercept) = %f" % xhat[0]
print "D (slope) = %f" % xhat[1]

e = b - np.dot(A, xhat)
enorm = np.linalg.norm(b-np.dot(A, xhat))

print "e (error) = %f" % enorm

fig = plt.figure()
plt.plot(fr.x, fr.y, "b+")
plt.plot(fr.x, xhat[0] + xhat[1]*fr.x, color="black")
plt.title("Team winning percentage per PM", fontsize=16)
plt.xlabel("PM", fontsize=16)
plt.ylabel("Team winning percentage", fontsize=16)
plt.text(-10, 0.7, "y = %1.3f + %1.3f*x" % (xhat[0], xhat[1]), fontsize=16)

fig.savefig('nba_reg.png', format="png")
plt.show()
