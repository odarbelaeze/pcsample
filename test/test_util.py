# -*- coding: utf-8 -*-

import numpy as np

from pcsample import in_circle_mask
from pcsample import out_circle_mask
from pcsample import in_circles_mask
from pcsample import out_circles_mask


def test_in_circle_mask_default():
    pos = np.array([[1, 0], [0, 0], ])
    cen = np.array([0, 0])
    assert (in_circle_mask(pos, cen, 0.5) == np.array([False, True])).all()


def test_in_circle_mask_square_circle():
    pos = np.array([
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 0],
        [2, 1],
        [2, 2],
        [2, 3],
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 3],
    ])
    cen = np.array([0.0, 0.0])
    rad = 3.0
    true = np.array([
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
    ])

    assert (in_circle_mask(pos, cen, rad) == true).all()


def test_out_circle_mask_default():
    pos = np.array([[1, 0], [0, 0], ])
    cen = np.array([0, 0])
    assert (out_circle_mask(pos, cen, 0.5) == np.array([True, False])).all()


def test_out_circle_mask_square_circle():
    pos = np.array([
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 0],
        [2, 1],
        [2, 2],
        [2, 3],
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 3],
    ])
    cen = np.array([0.0, 0.0])
    rad = 3.0
    true = np.array([
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        True,
        True,
        True,
    ])

    assert (out_circle_mask(pos, cen, rad) == true).all()


def test_in_circles_mask_default():
    pos = np.array([[1, 0], [0, 0], ])
    cens = (
        np.array([0.0, 0.0]),
        np.array([1.0, 1.0]),
    )
    assert (in_circles_mask(pos, cens, 0.5) == np.array([False, True])).all()


def test_in_circles_mask_square_circle():
    pos = np.array([
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 0],
        [2, 1],
        [2, 2],
        [2, 3],
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 3],
    ])
    cens = (
        np.array([0.0, 0.0]),
        np.array([1.0, 1.0]),
    )
    rad = 3.0
    true = np.array([
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ])

    assert (in_circles_mask(pos, cens, rad) == true).all()


def test_out_circles_mask_default():
    pos = np.array([[1, 0], [0, 0], ])
    cens = (
        np.array([0.0, 0.0]),
        np.array([1.0, 1.0]),
    )
    assert (out_circles_mask(pos, cens, 0.5) == np.array([True, False])).all()


def test_out_circles_mask_square_circle():
    pos = np.array([
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 0],
        [2, 1],
        [2, 2],
        [2, 3],
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 3],
    ])
    cens = (
        np.array([0.0, 0.0]),
        np.array([1.0, 1.0]),
    )
    rad = 3.0
    true = np.array([
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ])

    assert (out_circles_mask(pos, cens, rad) == true).all()
