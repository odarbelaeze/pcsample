# -*- coding: utf-8 -*-

import numpy as np

from pcsample import Sample


def test_macro_lattice_parameter_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)
    assert(s1.macro_lattice_parameter() == 1.0 * (2.0 * 5.0 + 4.0))
    assert(s2.macro_lattice_parameter() == 1.0 * (2.0 * 5.0 + 4.0))
    assert(s1.macro_lattice_parameter() == s2.macro_lattice_parameter())


def test_macro_lattice_parameter_changes_with_a():
    s1 = Sample(5.0, 4.0, 2.0, a=0.5)
    s2 = Sample(5.0, 4.0, 3.0, a=0.2)

    assert(s1.macro_lattice_parameter() == 0.5 * (2.0 * 5.0 + 4.0))
    assert(s2.macro_lattice_parameter() == 0.2 * (2.0 * 5.0 + 4.0))
    assert(s1.macro_lattice_parameter() != s2.macro_lattice_parameter())


def test_x_param_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    assert(s1.x_param() == s1.macro_lattice_parameter())
    assert(s2.x_param() == s2.macro_lattice_parameter())


def test_y_param_defaluts():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    sin120 = np.sin(np.radians(120))

    assert(s1.y_param() == (sin120 * s1.macro_lattice_parameter()))
    assert(s2.y_param() == (sin120 * s2.macro_lattice_parameter()))


def test_x_max_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    assert(s1.x_max() == (2.0 * s1.x_param()))
    assert(s2.x_max() == (3.0 * s2.x_param()))


def test_y_max_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    assert(s1.y_max() == (2.0 * s1.y_param()))
    assert(s2.y_max() == (3.0 * s2.y_param()))


def test_size_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    assert((s1.size() == np.array([s1.x_max(), s1.y_max(), ])).all())
    assert((s2.size() == np.array([s2.x_max(), s2.y_max(), ])).all())


def test_cell_size_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    assert((s1.cell_size() == np.array([s1.x_param(), s1.y_param(), ])).all())
    assert((s2.cell_size() == np.array([s2.x_param(), s2.y_param(), ])).all())


def test_super_cell_size_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    s1scz = np.array([s1.x_param(), 2.0 * s1.y_param(), ])
    s2scz = np.array([s2.x_param(), 2.0 * s2.y_param(), ])

    assert((s1.super_cell_size() == s1scz).all())
    assert((s2.super_cell_size() == s2scz).all())


def test_regular_lattice_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    s1reglat = s1.regular_lattice()
    s2reglat = s2.regular_lattice()

    assert((s1reglat < s1.size()).all())
    assert((s1reglat >= np.zeros(2)).all())

    assert((s2reglat < s2.size()).all())
    assert((s2reglat >= np.zeros(2)).all())


def test_random_lattice_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    s1reglat = s1.random_lattice()
    s2reglat = s2.random_lattice()

    assert((s1reglat < s1.size()).all())
    assert((s1reglat >= np.zeros(2)).all())

    assert((s2reglat < s2.size()).all())
    assert((s2reglat >= np.zeros(2)).all())


def test_centers_defaults():
    s1 = Sample(5.0, 4.0, 2.0)
    s2 = Sample(5.0, 4.0, 3.0)

    arrcenters1 = np.array(s1.centers())
    truthcenters1 = np.array((
        np.array([0.0, 0.0, ]) * s1.cell_size(),
        np.array([0.5, 1.0, ]) * s1.cell_size(),
        np.array([1.0, 0.0, ]) * s1.cell_size(),
        np.array([0.0, 2.0, ]) * s1.cell_size(),
        np.array([1.0, 2.0, ]) * s1.cell_size(),
    ))

    arrcenters2 = np.array(s2.centers())
    truthcenters2 = np.array((
        np.array([0.0, 0.0, ]) * s2.cell_size(),
        np.array([0.5, 1.0, ]) * s2.cell_size(),
        np.array([1.0, 0.0, ]) * s2.cell_size(),
        np.array([0.0, 2.0, ]) * s2.cell_size(),
        np.array([1.0, 2.0, ]) * s2.cell_size(),
    ))

    assert((arrcenters1 == truthcenters1).all())
    assert((arrcenters2 == truthcenters2).all())


def test_in_circles_rand_in_rand_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=True)
    assert(all([pos in s.random_lattice() for pos in s.in_circles()]))


def test_in_circles_reg_in_rand_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=True)
    assert(all([pos in s.regular_lattice() for pos in s.in_circles()]))


def test_in_circles_rand_in_reg_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=False)
    assert(all([pos in s.random_lattice() for pos in s.in_circles()]))


def test_in_circles_reg_in_reg_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=False)
    assert(all([pos in s.regular_lattice() for pos in s.in_circles()]))


def test_out_circles_rand_in_rand_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=True)
    assert(all([pos in s.random_lattice() for pos in s.out_circles()]))


def test_out_circles_reg_in_rand_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=True)
    assert(all([pos in s.random_lattice() for pos in s.out_circles()]))


def test_out_circles_rand_in_reg_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=False)
    assert(all([pos in s.regular_lattice() for pos in s.out_circles()]))


def test_out_circles_reg_in_reg_out():
    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=False)
    assert(all([pos in s.regular_lattice() for pos in s.out_circles()]))


def test_positions():
    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=False)
    assert(all([pos in s.regular_lattice() for pos in s.positions()]))

    s = Sample(5.0, 5.0, 2.0, in_rand=False, out_rand=True)
    assert(all([
        (pos in s.random_lattice() or pos in s.regular_lattice())
        for pos in s.positions()
    ]))

    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=False)
    assert(all([
        (pos in s.random_lattice() or pos in s.regular_lattice())
        for pos in s.positions()
    ]))

    s = Sample(5.0, 5.0, 2.0, in_rand=True, out_rand=True)
    assert(all([pos in s.random_lattice() for pos in s.positions()]))
