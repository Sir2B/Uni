import pylab

filename = "stats.txt"
data = pylab.loadtxt(filename, delimiter=',', dtype=int)
y_data = data[:, 0]
x_data = data[:, 1]
pylab.plot(x_data, y_data, '-o')
# pylab.show()
pylab.savefig('plot.png')
# pylab.legend()
# pylab.title("Title of Plot")
# pylab.xlabel("X Axis Label")
# pylab.ylabel("Y Axis Label")
pylab.close()
