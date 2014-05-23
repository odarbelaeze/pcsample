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
            self.rad
        )
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
        """
        Calls a script in the system responsible of creating the neighborhood
        files.
        """
        # TODO: Implement a little python interface for voro++ to leverage this
        #       subprocess call.
        from subprocess import call
        self.save(append_dims=1)
        call([
            script_name,
            str(self.x_max()), str(self.y_max()),
            self.temp_prefix,
        ])

    def load_info(self):
        """
        Load and returns the information created by the `compute_info`method
        returns a dictionary where the keys are the particle id and the values
        are yet another dictionary containing several useful data such as the
        neighborhood, and coordinates.
        """
        info = dict()

        coordinates = {
            'coordinates': open(self.temp_prefix, 'r'),
        }

        nb_files = {
            'np': open(self.temp_prefix + 'np.vol', 'r'),
            'fp': open(self.temp_prefix + 'pxpy.vol', 'r'),
            'px': open(self.temp_prefix + 'px.vol', 'r'),
            'py': open(self.temp_prefix + 'py.vol', 'r'),
        }

        for key in coordinates:
            for line in coordinates[key]:
                vertex_id = int(line.split()[0])
                pl = [float(number) for number in line.split()]
                info[vertex_id] = {key: np.array(pl[1:])}

        for key in nb_files:
            for line in nb_files[key]:
                pl = [int(number) for number in line.split()]
                vertex_id = pl[0]
                if key == 'fp' or key == 'np':
                    info[vertex_id][key] = [nb for nb in pl[1:] if nb > 0]
                else:
                    info[vertex_id][key] = [
                        nb for nb in pl[1:] if nb > 0
                        if nb not in info[vertex_id]['np']
                    ]

        return info

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
        return 'composed r{0!s} d{1!s} l{2!s} a{3!s}'.format(
            self.rad, self.d, self.l, self.a
        )

    def xml_unitcell(self, vertex_types=True, edge_types=True):
        info = self.load_info()
        n_cut = np.shape(self.in_circles())[0]

        cell_info = {
            'name': self.unitcell_name(),
            'dimension': '2',
            'vertices': str(len(info)),
        }
        unitcell = ETree.Element('UNITCELL', attrib=cell_info)

        for vid in info:
            attrib = {'id': str(vid + 1)}
            if vertex_types:
                attrib.update({'type': '1' if vid < n_cut else '2'})
            vertex = ETree.SubElement(unitcell, 'VERTEX', attrib=attrib)
            position = info[vid]['coordinates'][:2] / self.size()
            text = "{r[0]} {r[1]}".format(r=position)
            ETree.SubElement(vertex, 'COORDINATE').text = text

        def __offset_info(ri, rj, ox, oy):
            if ox or oy:
                offx = 0 if ox else 1 if (rj[0] < ri[0]) else - 1
                offy = 0 if oy else 1 if (rj[1] < ri[1]) else - 1
                return {'offset': str(offx) + ' ' + str(offy)}
            else:
                return dict()

        etype = 1

        for vid in info:
            for nbid in info[vid]['fp']:
                if nbid < vid:
                    continue

                edge_info = {}
                if edge_types:
                    edge_info.update({'type': str(etype)})
                    etype += 1

                vpos = info[vid]['coordinates']
                nbpos = info[nbid]['coordinates']
                ox = nbid in info[vid]['px']
                oy = nbid in info[vid]['py']

                edge = ETree.SubElement(unitcell, 'EDGE', attrib=edge_info)

                source_info = {'vertex': str(vid + 1)}
                offset_info = __offset_info(vpos, nbpos, ox, oy)
                target_info = {'vertex': str(nbid + 1)}
                target_info.update(offset_info)

                ETree.SubElement(edge, 'SOURCE', attrib=source_info)
                ETree.SubElement(edge, 'TARGET', attrib=target_info)

        return unitcell
