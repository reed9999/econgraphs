#Eventually read this: http://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
# not attempted yet.

#Following from https://matplotlib.org/examples/api/line_with_text.html
"""
=======================
Artist within an artist
=======================

Show how to override basic methods so an artist can contain another
artist.  In this case, the line contains a Text instance to label it.
"""
import numpy as np
import matplotlib.pyplot as plt
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

    def set_axes(self, axes):
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


fig, ax = plt.subplots()
#x, y = np.random.rand(2, 20)
x, y = [[0, 1, 2, 3, 4],
        [2, 3, 6, 13, 18],
        ]
x = np.divide(x, 100)
y = np.divide(y, 100)
line = MyLine(x, y, mfc='purple', ms=12, label='line label')
#line.text.set_text('line label')
line.text.set_color('green')
line.text.set_fontsize(16)

# https://stackoverflow.com/questions/23137991/matplotlib-get-and-set-axes-position
pos1 = ax.get_position() # get the original position 
pos2 = [pos1.x0 + 0.3, pos1.y0 + 0.3,  pos1.width / 2.0, pos1.height / 2.0] 
ax.set_position(pos2) # set a new position
#End that experimentation from stackoverflow

ax.add_line(line)
plt.show()
