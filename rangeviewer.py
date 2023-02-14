import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import List, Tuple

class Building():
    def __init__(self,
                 pos: Tuple[int],
                 size: int,
                 color: str='black',
                 rs: List[Tuple[float, str]] = []):

        self.pos = pos
        self.x, self.y = pos[0], pos[1]
        self.size = size
        self.color = color
        if isinstance(rs, tuple):
            rs = [rs]
        self.rs = rs
        self.greatest_r = max(r for r, _ in self.rs)
        self.linewidth=1.5

    def graph(self):
        # Contours
        self.ax.plot([self.x, self.x], [self.y, self.y+self.size],
                     [self.x, self.x+self.size], [self.y, self.y],
                     [self.x+self.size, self.x+self.size], [self.y, self.y+self.size],
                     [self.x, self.x+self.size], [self.y+self.size, self.y+self.size],
                     color=self.color, linewidth=self.linewidth)

        # Ranges
        for (r, c) in self.rs:
            self.ax.plot([self.x-r, self.x-r], [self.y, self.y+self.size],
                         [self.x, self.x+self.size], [self.y-r, self.y-r],
                         [self.x, self.x+self.size], [self.y+self.size+r, self.y+self.size+r],
                         [self.x+self.size+r, self.x+self.size+r], [self.y, self.y+self.size],
                         color=c, linewidth=self.linewidth)

            arc1 = patches.Arc(xy=self.pos, width=2*r, height=2*r,
                            theta1=180, theta2=270, linewidth=self.linewidth, color=c)
            arc2 = patches.Arc(xy=(self.x+self.size, self.y), width=2*r, height=2*r,
                            theta1=270, theta2=0, linewidth=self.linewidth, color=c)
            arc3 = patches.Arc(xy=(self.x, self.y+self.size), width=2*r, height=2*r,
                            theta1=90, theta2=180, linewidth=self.linewidth, color=c)
            arc4 = patches.Arc(xy=(self.x+self.size, self.y+self.size), width=2*r, height=2*r,
                            theta1=0, theta2=90, linewidth=self.linewidth, color=c)

            self.ax.add_patch(arc1)
            self.ax.add_patch(arc2)
            self.ax.add_patch(arc3)
            self.ax.add_patch(arc4)

class Village():
    def __init__(self, buildings_list: List[Building]):
        self.buildings_list = buildings_list
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        for building in self.buildings_list:
            building.ax = self.ax

    def graph(self):
        # Plot all the buildings
        for building in self.buildings_list:
            building.graph()

        self.ax.grid()

        minx = min(b.x-b.greatest_r for b in self.buildings_list)
        maxx = max(b.x+b.size+b.greatest_r for b in self.buildings_list)
        miny = min(b.y-b.greatest_r for b in self.buildings_list)
        maxy = max(b.y+b.size+b.greatest_r for b in self.buildings_list)
        span = max(maxx-minx, maxy-miny)
        self.ax.set_xlim((minx-1, minx+span+1))
        self.ax.set_ylim((miny-1, miny+span+1))

        self.ax.set_xticks(range(int(minx), int(minx+span+1)))
        self.ax.set_yticks(range(int(miny), int(miny+span+1)))

        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        plt.show()

if __name__=='__main__':

    tour1 = Building(pos=(0, 0), size=3, rs=[(2, 'mediumturquoise'), (4.7, 'sienna')])
    tour2 = Building(pos=(5, 7), size=4, rs=[(2, 'mediumturquoise'), (4.7, 'sienna')])

    village1 = Village(buildings_list=[tour1, tour2])

    village1.graph()
