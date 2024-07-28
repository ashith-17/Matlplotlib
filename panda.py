# Three lines to make our compiler able to draw:
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.legend()
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
