# -*- coding: utf-8 -*-

import lxml.etree as ETree
import numpy as np

from pcsample import Sample


def main():

    seed = 230514

    samples = [
        Sample(r, d, l, seed=seed)
        for r in [5, 10, 20]
        for d in [0, 5, 10]
        for l in range(2, 22, 2)
        if l * (2 * r + d) < 100
    ]

    lattices = ETree.Element('LATTICES')
    for sample in samples:
        sample.compute_info()
        lattices.append(sample.xml_lattice())
        lattices.append(sample.xml_unitcell())
        lattices.append(sample.xml_finite_lattice())
        lattices.append(sample.xml_latticegraph())

    with open('lattices.xml', 'w') as f:
        f.write(ETree.tostring(lattices, pretty_print=True))

    params = ''
    params += 'LATTICE_LIBRARY="../lattices.xml"' + '\n'
    params += 'MODEL="Ising"' + '\n'
    params += 'UPDATE="cluster"' + '\n'
    params += 'TERMALIZATION=50000' + '\n'
    params += 'SWEEPS=100000' + '\n'
    params += 'J=1' + '\n'
    params += 'SEED=' + str(seed) + '\n'

    params += '\n'.join(
        [
            '{LATTICE="' + sample.finite_lattice_name() + '";' +
            'T= ' + str(T) + ';}'
            for sample in samples
            for T in np.arange(1.0, 5.0, 0.1)
        ]
    )

    with open('params', 'w') as f:
        f.write(params)

if __name__ == '__main__':
    main()
