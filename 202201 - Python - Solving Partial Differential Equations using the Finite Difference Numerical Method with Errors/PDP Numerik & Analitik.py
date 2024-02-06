# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:33:06 2022

@author: csoen
"""

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as mpatches


#initializing a figure
fig = plt.figure()

# labeling the x axis and y axis
axis = plt.axes(xlim=(-100,100),ylim=(-100,100))

#initializing a line variable
line, = axis.plot([],[],lw=2)
line2, = axis.plot([],[],lw=2)



def animate(t):
    x1 = np.linspace(-1,1,201) 
    
    def f(z):
        return (1/6)*x1*(t)**3
    y1=2*f(x1[t])-f(x1[t-1])
    print(t)    
    
    

    x2 = np.linspace(-1,1,201)
    y2 = ((1/6)*(x2)*t**3)  
    
    line.set_data(x1,y1)
    line.set_linewidth(5)
    line.set_color('black')
    
    
    line2.set_data(x2,y2)
    line2.set_linestyle('dashed')
    line2.set_color('yellow')
    return line,line2


anim = animation.FuncAnimation(fig, animate, frames=15,
                               interval=100,blit=True)
fig.suptitle('Wave plot',fontsize=14)

black_patch = mpatches.Patch(color='black', label='Numerik')


yellow_patch = mpatches.Patch(color='yellow', label='Analitik')
axis.legend(handles=[yellow_patch,black_patch])



writervideo = animation.FFMpegWriter(fps=60)
anim.save('MetodeBedaHinggaPDP.mp4', writer=writervideo)
plt.show()