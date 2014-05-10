# -*- coding: utf-8 -*-

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
