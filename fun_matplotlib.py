#Eventually read this: http://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
# not attempted yet.

#TUTORIAL 1
#http://www.labri.fr/perso/nrougier/teaching/matplotlib/
import numpy as np
import matplotlib.pyplot as plt


# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
HALF = np.divide(X,2)


# Plot the above arrays.
plt.plot(X, C, color="orange", linewidth=4.5, linestyle=":")
plt.plot(X, S, color="red", linewidth=7.0, linestyle="-.")
plt.plot(X, HALF, color="blue", linewidth=3.0, linestyle="--")

# Set x limits
plt.xlim(-4.0,7.0)

#plt.xticks(np.linspace(-4,4,9,endpoint=True))
#plt.yticks(np.linspace(-1,1,5,endpoint=True))
plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])

# Set y limits
plt.ylim(-1.0,7.0)

# Set y ticks

# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)

# Show result on screen
plt.show()


#Another tutorial/example I played with:
# https://matplotlib.org/examples/api/line_with_text.html
# but ultimately that one was harder to tweak.
