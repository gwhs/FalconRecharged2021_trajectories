#!/usr/bin/env python3

import sys
import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ip
#import easygui


abspath = os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))

image_display_time = 3000

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="SeriesName")
args = parser.parse_args()

def close_event():
    plt.close()

def draw_line(data_file,line_color):
    data = pd.read_csv(data_file)
    x = data['X']
    y = data['Y']
    point = data['point']
    pointi = np.linspace(1, len(data), 100)

    xi = ip.CubicSpline(point, x, bc_type='clamped')
    yi = ip.CubicSpline(point, y, bc_type='clamped')

    ax.scatter(xm, ym, color='r', marker='*', linewidth=5, alpha=1)
    ax.plot(xi(pointi), yi(pointi), color=line_color, linewidth=5, alpha=0.5)
    ax.scatter(x, y, color='b', alpha=0.8, marker="x")
    ax.plot(x, y, color='b', alpha=0.2)
    for i, txt in enumerate(point):
        plt.annotate(txt, (x[i], y[i]))


markers_file = 'bounce_markers.csv'
data_file0= args.name + '_00.csv'
data_file1= args.name + '_01.csv'
data_file2= args.name + '_10.csv'
data_file3= args.name + '_11.csv'
data_file4= args.name + '_20.csv'
data_file5= args.name + '_21.csv'
data_file6= args.name + '_30.csv'
data_file7= args.name + '_31.csv'

out_file = args.name + '.png'

fig = plt.figure(dpi=300)  # facecolor='w', edgecolor='k')
timer = fig.canvas.new_timer(interval=image_display_time)
timer.add_callback(close_event)

ax = fig.add_subplot(1, 1, 1)

x_major_ticks = np.arange(0, 361, 30)
y_major_ticks = np.arange(-180, 1, 30)
ax.set_xticks(x_major_ticks)
ax.set_yticks(y_major_ticks)

ax.grid(which='both')
ax.set_xlim(0, 360)
ax.set_ylim(-180, 0)
ax.set_aspect(1)

markers = pd.read_csv(markers_file)
xm = markers['X']
ym = markers['Y']

draw_line(data_file0, 'g')
draw_line(data_file1, 'c')
draw_line(data_file2, 'y')
draw_line(data_file3, 'm')
draw_line(data_file4, 'b')
draw_line(data_file5, 'k')
draw_line(data_file6, 'c')
draw_line(data_file7, 'g')

plt.savefig(out_file,bbox_inches='tight')

timer.start()
plt.show()
print('result is saved as ' + out_file)

