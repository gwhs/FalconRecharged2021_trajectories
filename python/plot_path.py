#!/usr/bin/env python3

import sys
import getopt
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ip

image_display_time = 3000

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Name")
parser.add_argument("-i", "--csvfile", help="CSV name", default='data.csv')
args = parser.parse_args()


def close_event():
    plt.close()


if args.csvfile:
    data_file = args.csvfile
    out_file = data_file.split('.')[0] + '.png'
else:
    print('csvfile (-i)', 'challenge name (-n)')
if args.name:
    markers_file = args.name + '_markers.csv'
else:
    if 'slalom' in data_file.lower():
        markers_file = 'slalom_markers.csv'
    elif 'barrel' in data_file.lower():
        markers_file = 'barrel_markers.csv'
    elif 'bounce' in data_file.lower():
        markers_file = 'bounce_markers.csv'
    else:
        markers_file = 'markers.csv'

fig = plt.figure(dpi=240, facecolor='w', edgecolor='k')
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

data = pd.read_csv(data_file)
x = data['X']
y = data['Y']
point = data['point']
markers = pd.read_csv(markers_file)
xm = markers['X']
ym = markers['Y']
pointi = np.linspace(1, len(data), 100)

xi = ip.CubicSpline(point, x, bc_type='clamped')
yi = ip.CubicSpline(point, y, bc_type='clamped')
#xi = ip.CubicSpline(point,x,bc_type='natural')
#yi = ip.CubicSpline(point,y,bc_type='natural')
#xi = ip.interp1d(point,x)
#yi = ip.interp1d(point,y)
#xi = ip.interp1d(point,x,kind='cubic',)
#yi = ip.interp1d(point,y,kind='cubic',)

#xi = ip.interp1d(point,x,kind='quadratic',)
#yi = ip.interp1d(point,y,kind='quadratic',)
#xi = ip.PchipInterpolator(point,x)
#yi = ip.PchipInterpolator(point,y)
#xi = ip.Akima1DInterpolator(point,x)
#yi = ip.Akima1DInterpolator(point,y)

ax.scatter(xm, ym, color='r', marker='*', linewidth=5, alpha=1)
ax.plot(xi(pointi), yi(pointi), color='g', linewidth=5, alpha=0.5)
ax.scatter(x, y, color='b', alpha=0.5)
ax.plot(x, y, color='b', alpha=0.2)
for i, txt in enumerate(point):
    plt.annotate(txt, (x[i], y[i]))

plt.savefig(out_file)
print("TrajectoryHelper block:")
for v in data.values: 
    print('\t{'+str(v[1])+','+str(-1*v[2])+'},\t// '+str(v[0])) 

timer.start()
plt.show()
print('result is saved as ' + out_file)
