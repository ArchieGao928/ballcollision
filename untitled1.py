# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:50:42 2022

@author: Alienware
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Particle():
    def __init__(self, id = 0, r = np.zeros(2), v = np.zeros(2), R = 1E-2, m = 1, color = "blue"):
        self.id, self.r, self.v, self.R, self.m, self.color = id, r, v, R, m, color 
        
class Sim():
    
    X = 2
    Y = 2
    
    def __init__(self, dt = 1e-2, Np = 10):
        self.dt, self.Np = dt, Np
        self.particles = [Particle(i) for i in range(self.Np)]
        
    def increment(self):
        for particle in self.particles:
            particle.r += self.dt * particle.v
            
            
    def particle_positions(self):
        return [particle.r for particle in self.particles]
    
sim = Sim()

for particle in sim.particles:
    particle.r  = np.random.uniform([-sim.X/2, -sim.Y/2], [sim.X/2, sim.Y/2], 
                                    size = 2)
    particle.v = 1 * np.array([np.cos(np.pi/4), np.cos(np.pi/4)])
    
    
fig, ax = plt.subplots()
scatter = ax.scatter([], [])

def init():
    ax.set_xlim(-sim.X/2, sim.X/2)
    ax.set_ylim(-sim.Y/2, sim.Y/2)
    return scatter,

def update(frame):
    sim.increment()
    scatter.set_offsets(np.array(sim.particle_positions()))
    return scatter, 
ani = FuncAnimation(fig, update, frames=range(1200), init_func= init, 
                    blit = True, interval = 1/30, repeat = False)




