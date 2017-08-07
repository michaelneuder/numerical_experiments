#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class location(object):
    ''' an object describing current position '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + ', ' +str(self.z) + '>'

class walker(object):
    ''' an object which takes many random steps '''
    def __init__(self, identifier, start_loc):
        self.id = identifier
        self.current_loc = start_loc
        self.step_count = 0
        self.move_history = [self.current_loc]

    def take_step(self):
        self.step_count += 1
        delta_x, delta_y, delta_z = np.random.randn(3)
        self.current_loc = location(self.current_loc.get_x()+delta_x,
                                    self.current_loc.get_y()+delta_y,
                                    self.current_loc.get_z()+delta_z)
        self.move_history.append(self.current_loc)

    def get_id(self):
        return self.id

    def get_current_loc(self):
        return self.current_loc

    def get_step_count(self):
        return self.step_count

    def get_move_history(self):
        return self.move_history

    def __str__(self):
        return 'walker id: ' + str(self.id) + ' -- steps taken: ' + str(self.step_count) \
        + ' -- current location: ' + str(self.current_loc)

class space(object):
    ''' an object holding the locations of many walkers and their movements '''
    def __init__(self):
        self.walkers = {}
        self.walker_index = 0

    def add_walker(self):
        origin = location(0,0,0)
        self.walkers[self.walker_index] = walker(str(self.walker_index), origin)
        self.walker_index += 1

    def print_walkers(self):
        for walker in self.walkers:
            print(self.walkers[walker])

class simulation(object):
    ''' runs the simulation '''
    def __init__(self, num_walkers, num_steps, show_axis = 'on'):
        self.space_ = space()
        for i in range(num_walkers):
            self.space_.add_walker()
        for walker in self.space_.walkers:
            for step in range(num_steps):
                self.space_.walkers[walker].take_step()
            print(self.space_.walkers[walker])
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for walker in self.space_.walkers:
            hist = self.space_.walkers[walker].get_move_history()
            x_hist, y_hist, z_hist = [], [], []
            for move in hist:
                x, y, z = move.get_x(), move.get_y(), move.get_z()
                x_hist.append(x)
                y_hist.append(y)
                z_hist.append(z)
            ax.plot(x_hist, y_hist, z_hist, alpha=.5)
        plt.axis(show_axis)
        plt.show()
        exit()

def main():
    print('welcome to the random walker simulation. ')
    num_walkers = int(input('how many walkers do you want? '))
    num_steps = int(input('how many steps should each walker take? '))
    sim = simulation(num_walkers, num_steps)

if __name__ == '__main__':
    main()
