# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:50:42 2022
@author: Alienware
"""


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)

class Particle():
    def __init__(self, id = 0, r = np.zeros(2), v = np.zeros(2), R = 1E-2, m = 1, color = "blue"):
        self.id, self.r, self.v, self.R, self.m, self.color = id, r, v, R, m, color 
        
class Sim():
    
    X = 2
    Y = 2
    
    def __init__(self, dt = 1e-2, Np = 100):
        self.dt, self.Np = dt, Np
        self.particles = [Particle(i) for i in range(self.Np)]
        
    def collision_detection(self):
        ignore_list = []
        for particle1 in self.particles:
            x, y = particle1.r
            if ((x >= self.X/2 - particle1.R) or (x <= - self.X/2 + particle1.R)):
                particle1.v[0] *= -1
            if ((y >= self.Y/2 - particle1.R) or (y <= - self.Y/2 + particle1.R)):
                particle1.v[1] *= -1
                ### Blue Particle Range
            if ((particle1.color == "blue") and (x >= self.X/4 + particle1.R)):
                particle1.v[0] *= -1
            if ((particle1.color == "red") and (x <= - self.X/4 + particle1.R)):
                particle1.v[0] *= -1
            if particle1 in ignore_list:
                continue
###
            for particle2 in self.particles:
                if id(particle1) == id(particle2):
                    continue
                m1, m2 = particle1.m, particle2.m
                v1, v2 = particle1.v, particle2.v
                r1, r2 = particle1.r, particle2.r
                if np.dot(r1 - r2, r1 - r2) <= (particle1.R + particle2.R)**2:
                    v1_new = v1 - 2*m2/(m1+m2)*np.dot(v1-v2, r1-r2)/np.dot(r1-r2, r1-r2)* (r1-r2)
                    v2_new = v2 - 2*m1/(m1+m2)*np.dot(v2-v1, r2-r1)/np.dot(r2-r1, r2-r1)* (r2-r1)
                    particle1.v = v1_new
                    particle2.v = v2_new
                    ignore_list.append(particle2)
###            
    
                
        
        
    def increment(self):
        self.collision_detection()
        for particle in self.particles:
            particle.r += self.dt * particle.v
            
            
    def particle_positions(self):
        return [particle.r for particle in self.particles]
    
    def particle_colors(self):
        return [particle.color for particle in self.particles]
    
sim = Sim()


for i in range(int(sim.Np/2)):
    sim.particles[i].color = "red"
    
for particle in sim.particles:
    if particle.color == "blue":
        particle.r  = np.random.uniform([-sim.X/2, -sim.Y/2], [sim.X/4, sim.Y/2], 
                                        size = 2)
    else:
        particle.r  = np.random.uniform([-sim.X/4, -sim.Y/2], [sim.X/2, sim.Y/2], 
                                        size = 2)
    theta = np.random.random() * 2 * np.pi
    particle.v = 1 * np.array([np.cos(theta), np.cos(theta)])
    
#sim.particles[0].color = "red" 


    
    
fig, ax = plt.subplots()
plt.plot([0.5, 0.5], [-1, 1],color="blue")
plt.plot([-0.5,-0.5],[-1, 1],color="red")
scatter = ax.scatter([], [])

def init():
    ax.set_xlim(-sim.X/2, sim.X/2)
    ax.set_ylim(-sim.Y/2, sim.Y/2)
    return scatter,

def update(frame):
    sim.increment()
    scatter.set_offsets(np.array(sim.particle_positions()))
    scatter.set_color(sim.particle_colors())
    return scatter, 


ani = FuncAnimation(fig, update, frames=range(1200), init_func= init, 
                    blit = True, interval = 1/30, repeat = False)
