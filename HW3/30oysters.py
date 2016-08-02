import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fr = pd.read_csv("30oysters.txt", header=0)

fr['ones'] = 1

A = fr.as_matrix(['ones','Oyster_Weight_g'])
b = fr.as_matrix(['Oyster_Volume_cc'])

Atransp = np.transpose(A)
AtranspA = np.dot(Atransp, A)
AtranspA_inv = np.linalg.inv(AtranspA)
AtranspA_invAtransp = np.dot(AtranspA_inv, Atransp)
xhat = np.dot(AtranspA_invAtransp, b) #[C, D]

print "C (intercept) = %1.3f" % xhat[0]
print "D (slope) = %1.3f" % xhat[1]

e = b - np.dot(A, xhat)
enorm = np.linalg.norm(b-np.dot(A, xhat))

print "e (error) = %1.3f" % enorm

fig = plt.figure()
plt.plot(fr.Oyster_Weight_g, fr.Oyster_Volume_cc, "b+")
plt.plot(fr.Oyster_Weight_g, xhat[0] + xhat[1]*fr.Oyster_Weight_g, color="black")
plt.title("Oysters' volume as a function of their weight", fontsize=16)
plt.xlabel("Weight (g)", fontsize=16)
plt.ylabel("Volume (cc)", fontsize=16)
plt.text(6, 14, "y = %1.3f + %1.3f*x" % (xhat[0], xhat[1]), fontsize=16)

fig.savefig('30oysters_reg.png', format="png")
plt.show()
