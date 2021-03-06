from pylab import *
import matplotlib.pyplot as pyplot
import math

n = [2**x for x in range(2,13)]
times = [0.001918, 0.006392, 0.015157,
         0.013765, 0.053244, 0.204901,
         0.804681, 3.244271, 13.508356,
         57.598925, 252.237162]

fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)

line, = ax.plot(n, times, color='blue', lw=2)

ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)

ax.set_title('Time taken by eliminate as a function of matrix size', fontsize=16)
ax.set_xlabel('n', fontsize=16)
ax.set_ylabel('time (s)', fontsize=16)

fig.savefig('complexity.pdf', format="pdf")

show()

delta_y = math.log(times[-1], 2) - math.log(times[-6], 2)
delta_x = math.log(n[-1], 2) - math.log(n[-6], 2)
k = delta_y / delta_x

print "k = %f" % k
print "The time complexity is O(n^%d)" % k