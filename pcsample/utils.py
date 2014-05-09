import numpy as np


def in_circle_mask(positions, center, rad):
    """
    Returns a numpy mask of the positions laying inside the circle
    centered at `center` with radius `rad`.
    """
    # Accomplished trough Array broadcasting
    norms = np.sqrt(np.sum((positions - center) ** 2, axis=1))
    return norms <= rad


def out_circle_mask(positions, center, rad):
    """
    Returns a numpy mask of the positions laying outside the circle
    centered at `center` with radius `rad`.
    """
    # Accomplished using the DRY principle
    return np.logical_not(in_circle_mask(positions, center, rad))


def in_circles_mask(positions, centers, rad):
    """
    Returns a numpy mask of the positions laying inside of any of the
    circles centered at each `center` in `centers` with radius `rad`.
    """
    mask = np.empty(np.size(positions, axis=0), dtype=bool)
    mask.fill(False)

    for center in centers:
        mask = np.logical_or(mask, in_circle_mask(positions, center, rad))

    return mask


def out_circles_mask(positions, centers, rad):
    """
    Returns a numpy mask of the positions laying outside all the
    circles centered at each `center` in `centers` with radius `rad`.
    """
    # Accomplished using the DRY principle
    return np.logical_not(in_circles_mask(positions, centers, rad))
