# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt
#import lxml.etree as et
#from subprocess import call

# My own utilities

import utils


class Sample(object):
    """docstring for Sample"""
    def __init__(
        self, rad, d, l, a=1.0,
        tmpprefix="sample", in_rand=False, out_rand=True
    ):

        super(Sample, self).__init__()
        self.rad = rad
        self.d = d
        self.l = l
        self.a = a
        self.tmpprefix = tmpprefix
        self.in_rand = in_rand
        self.out_rand = out_rand

    def macro_lattice_parameter(self):
        """
        Returns the lattice parameter for the triangular lattice given
        the conditions.
        """
        return self.a * (2.0 * self.rad + self.d)

    def x_param(self):
        """
        Yields the lattice parameter in the x direction of the lattice.
        """
        return self.macro_lattice_parameter()

    def y_param(self):
        """
        Yields the lattice parameter in the y direction of the lattice.
        """
        return np.sin(np.radians(120)) * self.macro_lattice_parameter()

    def x_max(self):
        """
        Returns the maximum value of x.
        """
        return self.l * self.x_param()

    def y_max(self):
        """
        Returns the maximum value of y.
        """
        return self.l * self.y_param()

    def size(self):
        """
        Returns the sample size.
        """
        return np.array([self.x_max(), self.y_max(), ])

    def cell_size(self):
        """
        Returns the single cubic cell size.
        """
        return np.array([self.x_param(), self.y_param(), ])

    def super_cell_size(self):
        """
        Returns the dual in y cubic cell size.
        """
        return np.array([self.x_param(), 2.0 * self.y_param(), ])

    def regular_lattice(self):
        """
        Returns a regular lattice filling the whole sample.
        """
        # TODO: Cache this return
        xtics = np.arange(0.0, self.x_max(), self.a)
        ytics = np.arange(0.0, self.y_max(), self.a)
        return np.array([[x, y] for x in xtics for y in ytics])

    def random_lattice(self):
        """
        Returns a random lattice filling the whole sample.
        """
        #TODO: This may be a function, but I'm gessing is only used once
        n = int((self.l * (2 * self.rad + self.d)) ** 2)
        xrand = np.random.uniform(0, self.x_max(), n)
        yrand = np.random.uniform(0, self.y_max(), n)

        # TODO: Cache this return
        return np.column_stack((xrand, yrand))

    def centers(self):
        return (
            np.array([0.0, 0.0, ]) * self.cell_size(),
            np.array([0.5, 1.0, ]) * self.cell_size(),
            np.array([1.0, 0.0, ]) * self.cell_size(),
            np.array([0.0, 2.0, ]) * self.cell_size(),
            np.array([1.0, 2.0, ]) * self.cell_size(),
        )

    def in_circles(self):
        """
        Return the portion of the sample inside the circles.
        """
        if self.in_rand:
            positions = self.random_lattice()
        else:
            positions = self.regular_lattice()

        mask = utils.in_circles_mask(
            np.mod(positions, self.super_cell_size()),
            self.centers(),
            self.rad)
        return positions[mask]

    def out_circles(self):
        """
        Return the portion of the sample outside the circles.
        """
        if self.out_rand:
            positions = self.random_lattice()
        else:
            positions = self.regular_lattice()

        mask = utils.out_circles_mask(
            np.mod(positions, self.super_cell_size()),
            self.centers(),
            self.rad)
        return positions[mask]

    def positions(self):
        return np.vstack((self.in_circles(), self.out_circles()))
