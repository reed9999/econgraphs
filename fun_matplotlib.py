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
C=HALF

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="orange", linewidth=4.5, linestyle=":")

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="red", linewidth=7.0, linestyle="-.")

# Set x limits
plt.xlim(-4.0,17.0)

# Set x ticks
plt.xticks(np.linspace(-4,4,9,endpoint=True))

# Set y limits
plt.ylim(-1.0,1.0)

# Set y ticks
plt.yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)

# Show result on screen
plt.show()


#TUTORIAL (EXAMPLE) 2
#Following from https://matplotlib.org/examples/api/line_with_text.html
"""
=======================
Artist within an artist
=======================

Show how to override basic methods so an artist can contain another
artist.  In this case, the line contains a Text instance to label it.
"""
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext


class MyLine(lines.Line2D):
    def __init__(self, *args, **kwargs):
        # we'll update the position when the line data is set
        self.text = mtext.Text(0, 0, '')
        lines.Line2D.__init__(self, *args, **kwargs)

        # we can't access the label attr until *after* the line is
        # inited
        self.text.set_text(self.get_label())

    def set_figure(self, figure):
        self.text.set_figure(figure)
        lines.Line2D.set_figure(self, figure)

    #Doesn't appear this gets called in the example
    def arbitrary_name_set_axes(self, axes):
        self.text.set_axes(axes)
        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):
        # 2 pixel offset
        texttrans = transform + mtransforms.Affine2D().translate(2, 2)
        self.text.set_transform(texttrans)
        lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):
        if len(x):
            self.text.set_position((x[-1], y[-1]))

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        # draw my label at the end of the line with 2 pixel offset
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)

#Code for the example to exercise the class above.

# # fig, ax = plt.subplots()
# # #x, y = np.random.rand(2, 20)
# # x, y = [[0, 1, 2, 3, 4],
# #         [2, 3, 6, 13, 18],
# #         ]
# # x = np.divide(x, 100)
# # y = np.divide(y, 100)
# # line = MyLine(x, y, mfc='purple', ms=12, label='line label')
# # #line.text.set_text('line label')
# # line.text.set_color('green')
# # line.text.set_fontsize(16)
# # 
# # # https://stackoverflow.com/questions/23137991/matplotlib-get-and-set-axes-position
# # #Not that exciting, just moves them if I like.
# # #pos1 = ax.get_position() # get the original position 
# # #pos2 = [pos1.x0 + 0.3, pos1.y0 + 0.3,  pos1.width / 2.0, pos1.height / 2.0] 
# # #ax.set_position(pos2) # set a new position
# # #End that experimentation from stackoverflow
# # 
# # #Now I improvise a bit...
# # line.arbitrary_name_set_axes(ax)
# # #which causes this....
# # #C:\ProgramData\Anaconda3\lib\site-packages\matplotlib\artist.py:221: MatplotlibDeprecationWarning: set_axes has been deprecated in mpl 1.5, please use the
# # #axes property.  A removal date has not been set.
# #   #stacklevel=1)
# # 
# # ax.add_line(line)
# # plt.show()
