# -*- coding: utf-8 -*-

import numpy as np
# import matplotlib.pyplot as plt
import lxml.etree as ETree
# from subprocess import call

# My own utilities

import utils


class Sample(object):
    """docstring for Sample"""
    def __init__(
        self, rad, d, l, a=1.0,
        temp_prefix="sample", in_rand=False, out_rand=True,
        seed=2902
    ):

        super(Sample, self).__init__()
        self.rad = rad
        self.d = d
        self.l = l
        self.a = a
        self.temp_prefix = temp_prefix
        self.in_rand = in_rand
        self.out_rand = out_rand
        self.seed = seed

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
        # TODO: Cache regular_lattice lattice
        xtics = np.arange(0.0, self.x_max(), self.a)
        ytics = np.arange(0.0, self.y_max(), self.a)
        return np.array([[x, y] for x in xtics for y in ytics])

    def random_lattice(self):
        """
        Returns a random lattice filling the whole sample.
        """
        # TODO: Cache random lattice
        np.random.seed(self.seed)
        n = int((self.l * (2 * self.rad + self.d)) ** 2)
        xrand = np.random.uniform(0, self.x_max(), n)
        yrand = np.random.uniform(0, self.y_max(), n)

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
        # TODO: Cache in circles
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
        # TODO: Cache out circles
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
        """
        Returns the combined positions in and out circles.
        """
        return np.vstack((self.in_circles(), self.out_circles()))

    def to_string(self, include_id=True, append_dims=0):
        """
        Returns a csv like string wiht the positions, `include_id` switchs
        wether or not an additional column is included with a number for each
        position.
        """
        if include_id:
            lst = [
                ('%i %f %f' + ' 0' * append_dims) % (i, r[0], r[1])
                for i, r in enumerate(self.positions())
            ]
        else:
            lst = ['%f %f' % (r[0], r[1]) for r in self.positions()]
        return '\n'.join(lst)

    def save(self, **kwargs):
        """
        Saves a csv like file wiht the positions, `kwargs` are passed up
        to the `to_string` method.
        """
        # TODO: Check dependency, if the file is already created,
        # maybe save some timestamp
        with open(self.temp_prefix, 'w') as f:
            f.write(self.to_string(**kwargs))

    def compute_info(self, script_name='vorop.sh'):
        from sys import call
        self.save(append_dims=1)
        call([
            script_name,
            str(self.x_max()), str(self.y_max()),
            self.temp_prefix,
        ])

    def load_info(self):
        pass

    def lattice_name(self):
        return 'square hex r{0!s} d{1!s} l{2!s} a{3!s}'.format(
            self.rad, self.d, self.l, self.a
        )

    def xml_lattice(self):
        lattice = ETree.Element('LATTICE', attrib={
            'dimension': '2',
            'name': self.lattice_name()
        })
        basis = ETree.SubElement(lattice, 'BASIS')
        ETree.SubElement(basis, 'VECTOR').text = "%f 0" % self.x_max()
        ETree.SubElement(basis, 'VECTOR').text = "0 %f" % self.y_max()

        return lattice

    def finite_lattice_name(self):
        return 'single square hex r{0!s} d{1!s} l{2!s} a{3!s}'.format(
            self.rad, self.d, self.l, self.a
        )

    def xml_finite_lattice(self, ref_lattice=True):
        finite_lattice = ETree.Element('FINITELATTICE', attrib={
            'name': self.finite_lattice_name(),
            'dimension': '2'
        })

        if ref_lattice:
            ETree.SubElement(finite_lattice, 'LATTICE', attrib={
                'ref': self.lattice_name()
            })
        else:
            finite_lattice.append(self.xml_lattice())

        ETree.SubElement(finite_lattice, 'EXTENT', attrib={
            'dimension': '1',
            'size': '1'
        })
        ETree.SubElement(finite_lattice, 'EXTENT', attrib={
            'dimension': '2',
            'size': '1'
        })
        ETree.SubElement(finite_lattice, 'BOUNDARY', attrib={
            'type': 'periodic'
        })
        return finite_lattice

    def unitcell_name(self):
        pass

    def xml_unitcell(self, vertex_types=True, edge_types=True):
        pass
