import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

operations = ["remove_insert","random_access"]

for operation in operations:
  compare = np.loadtxt("results/"+operation)
  p1, = plt.plot(compare[:,0],compare[:,1],label="Vector")
  p2, = plt.plot(compare[:,0],compare[:,2],label="List")

  plt.legend(handler_map={p2: HandlerLine2D(numpoints=4)})
  plt.xlabel("# elements")
  plt.ylabel("run time")
  #plt.show()
  plt.savefig("results/plot_random_"+operation+".png")
  plt.clf()
