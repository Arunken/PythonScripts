# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:40:52 2018

@author: Ourabora
"""

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.xlabel('random')
plt.show()

plt.plot([1,2,3,4],[1,10,9,16])


import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,18,9,16],'ro') # bo gives blue color dots
plt.axis([0,6,0,20])
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0.,5.,0.2)

# red dashes, blue squares and green triangles
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()

# multiplots and axis
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

# pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(2,1,2)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()


import matplotlib.pyplot as plt
plt.figure(1) # the first figure
plt.subplot(211) # the first subplot in the first figure
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(2) # a second figure
plt.plot([4,5,6]) #creates a subplot(111) by default

plt.figure(1) # figure 1 current; subplot(212) still current
plt.title('Easy as 1, 2, 3') 


# working with text in plot s
import numpy as np
import matplotlib.pyplot as plt

# fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x,50,normed=1,facecolor='g',alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.010,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()


# text properties in pyplots
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


# axes coordinates are 0,0 is bottom left and 1,1 is upper right
p = patches.Rectangle(
        (left,bottom),width,height,
        fill=False,transform=ax.transAxes,clip_on=False
        )

ax.add_patch(p)

ax.text(left,bottom,'left top',
        horizontalalignment='left',
        verticalalignment='top',
        transform = ax.transAxes)

ax.text(left,bottom,'left bottom',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes)

ax.text(right, top,'right bottom',
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes)

ax.text(right,top,'right top',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(right,bottom,'center top',
        horizontalalignment='center',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(left,0.5*(bottom+top),'right center',
        horizontalalignment='right',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)


ax.text(left,0.5*(bottom+top),'left center',
        horizontalalignment='left',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)

ax.text(0.5*(left+right),0.5*(bottom+top),'middle',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20,color='red',
        transform=ax.transAxes)


ax.text(right,0.5*(bottom+top),'centered',
        horizontalalignment='center',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)

ax.text(left,top,'rotated\nwith newlines',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=45,
        transform=ax.transAxes)

ax.set_axis_off()
plt.show()


# annotating texts 
import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0,5.0,0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t,s,lw=2)

plt.annotate('local max',xy=(2,1),xytext=(3,1.5),
             arrowprops=dict(facecolor='black',shrink=0.05),
             )

plt.ylim(-2,2)
plt.show()


# log and non linear axis
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter # useful for 'logit' scale

# Fixing random state for reproducibility

np.random.seed(19680801)

# make up some data in the interval 0,1
y = np.random.nrmal(loc=0.5, scaple=0.4,size=1000)
y = y[(y>0) & (y<1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# Symmetric log
plt.subplot(223)
plt.plot(x,y,-y.mean())
plt.yscale('syslog',linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.grid(True)


# format the minor tick of the y-axis into empty strings with 
# NullFormatter , to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92,bottom=0.08,left=0.10,right=0.95,hspace = 0.25,
                    wspace=0.35)






