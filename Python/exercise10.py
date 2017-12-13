import matplotlib.pyplot as mpl
import numpy as np

mpl.title("Exercise 10 Function")
mpl.xlabel("X")
mpl.ylabel("f(x) =  sin^2(x-2)e^(-x^2)")

x = np.arange(0,3)
y = (np.sin(x-2) ** 2) * (np.e ** (-x ** 2))

mpl.plot(x,y)
mpl.show()
