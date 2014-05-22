# -*- coding: utf-8 -*-

import numpy as np

from pcsample import Sample


STRING_2_2_2_id = """\
0 0.000000 0.000000
1 0.000000 1.000000
2 0.000000 2.000000
3 0.000000 9.000000
4 0.000000 10.000000
5 1.000000 0.000000
6 1.000000 1.000000
7 1.000000 9.000000
8 1.000000 10.000000
9 2.000000 0.000000
10 2.000000 4.000000
11 2.000000 5.000000
12 2.000000 6.000000
13 3.000000 4.000000
14 3.000000 5.000000
15 3.000000 6.000000
16 3.000000 7.000000
17 4.000000 0.000000
18 4.000000 4.000000
19 4.000000 5.000000
20 4.000000 6.000000
21 5.000000 0.000000
22 5.000000 1.000000
23 5.000000 9.000000
24 5.000000 10.000000
25 6.000000 0.000000
26 6.000000 1.000000
27 6.000000 2.000000
28 6.000000 9.000000
29 6.000000 10.000000
30 7.000000 0.000000
31 7.000000 1.000000
32 7.000000 9.000000
33 7.000000 10.000000
34 8.000000 0.000000
35 8.000000 4.000000
36 8.000000 5.000000
37 8.000000 6.000000
38 9.000000 4.000000
39 9.000000 5.000000
40 9.000000 6.000000
41 9.000000 7.000000
42 10.000000 0.000000
43 10.000000 4.000000
44 10.000000 5.000000
45 10.000000 6.000000
46 11.000000 0.000000
47 11.000000 1.000000
48 11.000000 9.000000
49 11.000000 10.000000
50 8.173270 2.492228
51 6.816241 6.621154
52 6.883402 2.755739
53 8.737827 9.293355
54 8.287426 8.203952
55 9.039811 0.665320
56 5.947309 5.454306
57 3.421944 9.162209
58 6.127650 6.677901
59 8.952020 8.633043
60 11.533152 8.215356
61 5.678841 6.522786
62 3.415932 2.257554
63 9.529698 2.966346
64 3.800759 1.390208
65 1.357697 7.730228
66 9.642399 8.249615
67 0.864202 2.593632
68 8.187937 7.862357
69 9.906344 8.023674
70 8.389654 9.674626
71 1.774653 7.616606
72 11.673113 4.084108
73 1.057870 2.226151
74 2.794770 7.812554
75 1.908879 3.401869
76 8.865346 7.925502
77 11.388308 5.813421
78 7.726603 1.460103
79 4.420407 6.988900
80 5.112401 8.084635
81 9.152581 9.107077
82 0.696605 4.409674
83 6.742200 4.257955
84 5.312925 7.277918
85 9.975471 6.983342
86 7.193368 8.584019
87 3.298118 2.985360
88 0.869716 6.018266
89 7.882797 2.442746
90 5.559329 7.465366
91 7.940100 9.409426
92 7.005560 5.968762
93 9.001977 9.234026
94 2.192285 1.284963
95 0.431326 4.269499
96 9.571195 3.161973
97 1.793398 8.352598
98 6.617838 8.132496
99 9.487027 7.283405
100 10.203263 1.966146
101 0.702222 2.265513
102 3.242297 9.989684
103 3.179244 9.294601
104 1.608784 8.957513
105 6.827849 6.926306
106 7.524679 8.586315
107 9.146506 2.612103
108 6.781053 6.250603
109 2.015902 2.956837
110 2.054594 7.224545
111 2.599711 0.335255
112 9.155907 0.528067
113 4.109585 0.665776
114 11.068180 4.933080
115 1.670491 9.021622
116 9.202781 2.011522
117 3.898727 9.534230
118 2.631690 7.682275
119 8.115271 8.716049
120 3.911436 2.486958
121 8.320459 0.995696
122 4.078857 3.387685
123 10.670385 3.594555
124 0.817694 7.947013
125 10.134362 2.809378
126 2.405473 3.195753
127 11.627874 7.885213
128 3.025541 10.099834
129 8.003986 0.407578
130 1.514581 1.542137
131 0.170365 3.874633
132 6.303232 4.249357
133 8.219924 1.555487
134 1.106431 7.482676\
"""

STRING_2_2_2_no_id = """\
0.000000 0.000000
0.000000 1.000000
0.000000 2.000000
0.000000 9.000000
0.000000 10.000000
1.000000 0.000000
1.000000 1.000000
1.000000 9.000000
1.000000 10.000000
2.000000 0.000000
2.000000 4.000000
2.000000 5.000000
2.000000 6.000000
3.000000 4.000000
3.000000 5.000000
3.000000 6.000000
3.000000 7.000000
4.000000 0.000000
4.000000 4.000000
4.000000 5.000000
4.000000 6.000000
5.000000 0.000000
5.000000 1.000000
5.000000 9.000000
5.000000 10.000000
6.000000 0.000000
6.000000 1.000000
6.000000 2.000000
6.000000 9.000000
6.000000 10.000000
7.000000 0.000000
7.000000 1.000000
7.000000 9.000000
7.000000 10.000000
8.000000 0.000000
8.000000 4.000000
8.000000 5.000000
8.000000 6.000000
9.000000 4.000000
9.000000 5.000000
9.000000 6.000000
9.000000 7.000000
10.000000 0.000000
10.000000 4.000000
10.000000 5.000000
10.000000 6.000000
11.000000 0.000000
11.000000 1.000000
11.000000 9.000000
11.000000 10.000000
8.173270 2.492228
6.816241 6.621154
6.883402 2.755739
8.737827 9.293355
8.287426 8.203952
9.039811 0.665320
5.947309 5.454306
3.421944 9.162209
6.127650 6.677901
8.952020 8.633043
11.533152 8.215356
5.678841 6.522786
3.415932 2.257554
9.529698 2.966346
3.800759 1.390208
1.357697 7.730228
9.642399 8.249615
0.864202 2.593632
8.187937 7.862357
9.906344 8.023674
8.389654 9.674626
1.774653 7.616606
11.673113 4.084108
1.057870 2.226151
2.794770 7.812554
1.908879 3.401869
8.865346 7.925502
11.388308 5.813421
7.726603 1.460103
4.420407 6.988900
5.112401 8.084635
9.152581 9.107077
0.696605 4.409674
6.742200 4.257955
5.312925 7.277918
9.975471 6.983342
7.193368 8.584019
3.298118 2.985360
0.869716 6.018266
7.882797 2.442746
5.559329 7.465366
7.940100 9.409426
7.005560 5.968762
9.001977 9.234026
2.192285 1.284963
0.431326 4.269499
9.571195 3.161973
1.793398 8.352598
6.617838 8.132496
9.487027 7.283405
10.203263 1.966146
0.702222 2.265513
3.242297 9.989684
3.179244 9.294601
1.608784 8.957513
6.827849 6.926306
7.524679 8.586315
9.146506 2.612103
6.781053 6.250603
2.015902 2.956837
2.054594 7.224545
2.599711 0.335255
9.155907 0.528067
4.109585 0.665776
11.068180 4.933080
1.670491 9.021622
9.202781 2.011522
3.898727 9.534230
2.631690 7.682275
8.115271 8.716049
3.911436 2.486958
8.320459 0.995696
4.078857 3.387685
10.670385 3.594555
0.817694 7.947013
10.134362 2.809378
2.405473 3.195753
11.627874 7.885213
3.025541 10.099834
8.003986 0.407578
1.514581 1.542137
0.170365 3.874633
6.303232 4.249357
8.219924 1.555487
1.106431 7.482676\
"""


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


def test_to_string_defaults():
    s = Sample(2, 2, 2)
    correct = STRING_2_2_2_id
    assert(s.to_string() == correct)


def test_to_string_no_id():
    s = Sample(2, 2, 2)
    correct = STRING_2_2_2_no_id
    assert(s.to_string(include_id=False) == correct)


def test_save_creates_file():
    fname = 'test_file'
    s = Sample(2, 2, 2, temp_prefix=fname)
    s.save()

    import os
    assert(os.path.isfile(fname))
    os.remove(fname)


def test_save_writes_right_results_id():
    fname = 'test_file'
    s = Sample(2, 2, 2, temp_prefix=fname)
    s.save()

    import os
    with open(fname, 'r') as f:
        assert(f.read() == STRING_2_2_2_id)
    os.remove(fname)


def test_save_writes_right_results_no_id():
    fname = 'test_sample'
    s = Sample(2, 2, 2, temp_prefix=fname)
    s.save(include_id=False)

    import os
    with open(fname, 'r') as f:
        assert(f.read() == STRING_2_2_2_no_id)
    os.remove(fname)


def test_compute_info_writes_files():
    import os
    prefix = 'test_sample'
    s = Sample(2, 2, 2, temp_prefix=prefix)
    s.compute_info()
    sufixes = [
        'pxpy.vol',
        'px.vol',
        'py.vol',
        'np.vol',
        '.vol',
        '.gnu',
    ]
    assert(all([os.path.isfile(prefix + sufix) for sufix in sufixes]))
    map(os.remove, [prefix + sufix for sufix in sufixes])
    os.remove(prefix)


def test_load_info_defaults():
    s = Sample(2, 2, 2)
    info_ref = {
        0: {
            'coordinates': np.array([0., 0., 0.]),
            'np': [5, 1],
            'px': [46],
            'py': [4]
        },
        1: {
            'coordinates': np.array([0., 1., 0.]),
            'np': [2, 6],
            'px': [47],
            'py': []
        },
        2: {
            'coordinates': np.array([0., 2., 0.]),
            'np': [67, 6, 101, 1],
            'px': [125, 123, 100, 47, 131],
            'py': []
        },
        3: {
            'coordinates': np.array([0., 9., 0.]),
            'np': [124, 7, 4],
            'px': [48, 60],
            'py': []
        },
        4: {
            'coordinates': np.array([0., 10., 0.]),
            'np': [8, 3],
            'px': [49],
            'py': []
        },
        5: {
            'coordinates': np.array([1., 0., 0.]),
            'np': [9, 6],
            'px': [],
            'py': [8]
        },
        6: {
            'coordinates': np.array([1., 1., 0.]),
            'np': [5, 1, 2, 130, 73, 9, 101, 94],
            'px': [],
            'py': []
        },
        7: {
            'coordinates': np.array([1., 9., 0.]),
            'np': [97, 104, 8, 3, 124, 115],
            'px': [],
            'py': []
        },
        8: {
            'coordinates': np.array([1., 10., 0.]),
            'np': [7, 4, 128, 115],
            'px': [],
            'py': [9, 5]
        },
        9: {
            'coordinates': np.array([2., 0., 0.]),
            'np': [6, 94, 111, 5],
            'px': [],
            'py': [128, 115, 8]
        },
        10: {
            'coordinates': np.array([2., 4., 0.]),
            'np': [126, 13, 11, 82, 75],
            'px': [],
            'py': []
        },
        11: {
            'coordinates': np.array([2., 5., 0.]),
            'np': [14, 10, 12, 88, 82],
            'px': [],
            'py': []
        },
        12: {
            'coordinates': np.array([2., 6., 0.]),
            'np': [11, 15, 88, 110, 16],
            'px': [],
            'py': []
        },
        13: {
            'coordinates': np.array([3., 4., 0.]),
            'np': [122, 18, 14, 10, 126, 87],
            'px': [],
            'py': []
        },
        14: {
            'coordinates': np.array([3., 5., 0.]),
            'np': [13, 11, 15, 19],
            'px': [],
            'py': []
        },
        15: {
            'coordinates': np.array([3., 6., 0.]),
            'np': [14, 20, 16, 12],
            'px': [],
            'py': []
        },
        16: {
            'coordinates': np.array([3., 7., 0.]),
            'np': [20, 15, 118, 110, 74, 79, 12],
            'px': [],
            'py': []
        },
        17: {
            'coordinates': np.array([4., 0., 0.]),
            'np': [21, 111, 113],
            'px': [],
            'py': [24, 102, 117, 128]
        },
        18: {
            'coordinates': np.array([4., 4., 0.]),
            'np': [132, 122, 13, 19],
            'px': [],
            'py': []
        },
        19: {
            'coordinates': np.array([4., 5., 0.]),
            'np': [20, 56, 14, 132, 18],
            'px': [],
            'py': []
        },
        20: {
            'coordinates': np.array([4., 6., 0.]),
            'np': [16, 79, 15, 19, 56, 61],
            'px': [],
            'py': []
        },
        21: {
            'coordinates': np.array([5., 0., 0.]),
            'np': [25, 113, 17, 22],
            'px': [],
            'py': [24]
        },
        22: {
            'coordinates': np.array([5., 1., 0.]),
            'np': [27, 26, 21, 113, 64, 120],
            'px': [],
            'py': []
        },
        23: {
            'coordinates': np.array([5., 9., 0.]),
            'np': [80, 28, 24, 57, 117],
            'px': [],
            'py': []
        },
        24: {
            'coordinates': np.array([5., 10., 0.]),
            'np': [29, 117, 23],
            'px': [],
            'py': [21, 17]
        },
        25: {
            'coordinates': np.array([6., 0., 0.]),
            'np': [30, 21, 26],
            'px': [],
            'py': [29]
        },
        26: {
            'coordinates': np.array([6., 1., 0.]),
            'np': [31, 27, 22, 25],
            'px': [],
            'py': []
        },
        27: {
            'coordinates': np.array([6., 2., 0.]),
            'np': [132, 52, 31, 22, 120, 26, 122],
            'px': [],
            'py': []
        },
        28: {
            'coordinates': np.array([6., 9., 0.]),
            'np': [80, 23, 29, 32, 98],
            'px': [],
            'py': []
        },
        29: {
            'coordinates': np.array([6., 10., 0.]),
            'np': [33, 24, 28],
            'px': [],
            'py': [25]
        },
        30: {
            'coordinates': np.array([7., 0., 0.]),
            'np': [34, 31, 25, 129],
            'px': [],
            'py': [33]
        },
        31: {
            'coordinates': np.array([7., 1., 0.]),
            'np': [129, 78, 26, 30, 27, 52],
            'px': [],
            'py': []
        },
        32: {
            'coordinates': np.array([7., 9., 0.]),
            'np': [98, 86, 28, 33, 91, 106],
            'px': [],
            'py': []
        },
        33: {
            'coordinates': np.array([7., 10., 0.]),
            'np': [91, 70, 29, 32],
            'px': [],
            'py': [30, 34]
        },
        34: {
            'coordinates': np.array([8., 0., 0.]),
            'np': [112, 129, 30, 55],
            'px': [],
            'py': [33, 70, 91]
        },
        35: {
            'coordinates': np.array([8., 4., 0.]),
            'np': [89, 52, 83, 36, 38, 50],
            'px': [],
            'py': []
        },
        36: {
            'coordinates': np.array([8., 5., 0.]),
            'np': [39, 35, 83, 92, 37],
            'px': [],
            'py': []
        },
        37: {
            'coordinates': np.array([8., 6., 0.]),
            'np': [41, 40, 51, 92, 36, 68, 105],
            'px': [],
            'py': []
        },
        38: {
            'coordinates': np.array([9., 4., 0.]),
            'np': [96, 43, 35, 39, 50, 107],
            'px': [],
            'py': []
        },
        39: {
            'coordinates': np.array([9., 5., 0.]),
            'np': [44, 38, 36, 40],
            'px': [],
            'py': []
        },
        40: {
            'coordinates': np.array([9., 6., 0.]),
            'np': [39, 45, 37, 41, 85],
            'px': [],
            'py': []
        },
        41: {
            'coordinates': np.array([9., 7., 0.]),
            'np': [85, 40, 68, 76, 99, 37],
            'px': [],
            'py': []
        },
        42: {
            'coordinates': np.array([10., 0., 0.]),
            'np': [112, 46, 47],
            'px': [],
            'py': [48, 81, 93, 49]
        },
        43: {
            'coordinates': np.array([10., 4., 0.]),
            'np': [123, 96, 44, 38, 114],
            'px': [],
            'py': []
        },
        44: {
            'coordinates': np.array([10., 5., 0.]),
            'np': [43, 39, 45, 114],
            'px': [],
            'py': []
        },
        45: {
            'coordinates': np.array([10., 6., 0.]),
            'np': [44, 40, 85, 77, 114],
            'px': [],
            'py': []
        },
        46: {
            'coordinates': np.array([11., 0., 0.]),
            'np': [42, 47],
            'px': [],
            'py': [49]
        },
        47: {
            'coordinates': np.array([11., 1., 0.]),
            'np': [46, 123, 100, 112, 42, 72],
            'px': [2, 1],
            'py': []
        },
        48: {
            'coordinates': np.array([11., 9., 0.]),
            'np': [60, 81, 49, 69, 66],
            'px': [3],
            'py': [42]
        },
        49: {
            'coordinates': np.array([11., 10., 0.]),
            'np': [48, 93, 81],
            'px': [4],
            'py': [42, 46]
        },
        50: {
            'coordinates': np.array([8.17327, 2.492228, 0.]),
            'np': [133, 89, 38, 35, 116, 107],
            'px': [],
            'py': []
        },
        51: {
            'coordinates': np.array([6.816241, 6.621154, 0.]),
            'np': [108, 58, 105, 37, 92],
            'px': [],
            'py': []
        },
        52: {
            'coordinates': np.array([6.883402, 2.755739, 0.]),
            'np': [83, 35, 78, 89, 31, 27, 132],
            'px': [],
            'py': []
        },
        53: {
            'coordinates': np.array([8.737827, 9.293355, 0.]),
            'np': [119, 91, 70, 93, 59],
            'px': [],
            'py': []
        },
        54: {
            'coordinates': np.array([8.287426, 8.203952, 0.]),
            'np': [76, 68, 106, 59, 119],
            'px': [],
            'py': []
        },
        55: {
            'coordinates': np.array([9.039811, 0.66532, 0.]),
            'np': [129, 121, 34, 112, 100, 116],
            'px': [],
            'py': []
        },
        56: {
            'coordinates': np.array([5.947309, 5.454306, 0.]),
            'np': [83, 92, 132, 19, 20, 61, 108, 58],
            'px': [],
            'py': []
        },
        57: {
            'coordinates': np.array([3.421944, 9.162209, 0.]),
            'np': [80, 23, 117, 74, 103],
            'px': [],
            'py': []
        },
        58: {
            'coordinates': np.array([6.12765, 6.677901, 0.]),
            'np': [56, 108, 90, 61, 105, 51],
            'px': [],
            'py': []
        },
        59: {
            'coordinates': np.array([8.95202, 8.633043, 0.]),
            'np': [54, 76, 53, 119, 93, 66, 81],
            'px': [],
            'py': []
        },
        60: {
            'coordinates': np.array([11.533152, 8.215356, 0.]),
            'np': [127, 48, 69],
            'px': [124, 3],
            'py': []
        },
        61: {
            'coordinates': np.array([5.678841, 6.522786, 0.]),
            'np': [79, 20, 90, 84, 56, 58],
            'px': [],
            'py': []
        },
        62: {
            'coordinates': np.array([3.415932, 2.257554, 0.]),
            'np': [64, 94, 87, 120, 126, 109],
            'px': [],
            'py': []
        },
        63: {
            'coordinates': np.array([9.529698, 2.966346, 0.]),
            'np': [96, 107, 125],
            'px': [],
            'py': []
        },
        64: {
            'coordinates': np.array([3.800759, 1.390208, 0.]),
            'np': [113, 22, 62, 120, 111, 94],
            'px': [],
            'py': []
        },
        65: {
            'coordinates': np.array([1.357697, 7.730228, 0.]),
            'np': [71, 134, 97, 124],
            'px': [],
            'py': []
        },
        66: {
            'coordinates': np.array([9.642399, 8.249615, 0.]),
            'np': [48, 81, 59, 99, 76, 69],
            'px': [],
            'py': []
        },
        67: {
            'coordinates': np.array([0.864202, 2.593632, 0.]),
            'np': [131, 109, 73, 101, 2, 75],
            'px': [],
            'py': []
        },
        68: {
            'coordinates': np.array([8.187937, 7.862357, 0.]),
            'np': [76, 54, 106, 98, 86, 41, 105, 37],
            'px': [],
            'py': []
        },
        69: {
            'coordinates': np.array([9.906344, 8.023674, 0.]),
            'np': [127, 60, 99, 85, 66, 48],
            'px': [],
            'py': []
        },
        70: {
            'coordinates': np.array([8.389654, 9.674626, 0.]),
            'np': [53, 91, 33, 93],
            'px': [],
            'py': [112, 34]
        },
        71: {
            'coordinates': np.array([1.774653, 7.616606, 0.]),
            'np': [134, 65, 97, 118, 110],
            'px': [],
            'py': []
        },
        72: {
            'coordinates': np.array([11.673113, 4.084108, 0.]),
            'np': [47, 123, 114],
            'px': [131, 95],
            'py': []
        },
        73: {
            'coordinates': np.array([1.05787, 2.226151, 0.]),
            'np': [101, 67, 6, 130, 109],
            'px': [],
            'py': []
        },
        74: {
            'coordinates': np.array([2.79477, 7.812554, 0.]),
            'np': [16, 118, 103, 57, 79, 97, 80],
            'px': [],
            'py': []
        },
        75: {
            'coordinates': np.array([1.908879, 3.401869, 0.]),
            'np': [109, 126, 67, 131, 10, 82],
            'px': [],
            'py': []
        },
        76: {
            'coordinates': np.array([8.865346, 7.925502, 0.]),
            'np': [99, 41, 54, 59, 66, 68],
            'px': [],
            'py': []
        },
        77: {
            'coordinates': np.array([11.388308, 5.813421, 0.]),
            'np': [114, 85, 45, 127],
            'px': [82, 88, 95],
            'py': []
        },
        78: {
            'coordinates': np.array([7.726603, 1.460103, 0.]),
            'np': [129, 121, 133, 52, 31, 89],
            'px': [],
            'py': []
        },
        79: {
            'coordinates': np.array([4.420407, 6.9889, 0.]),
            'np': [84, 61, 74, 80, 16, 20],
            'px': [],
            'py': []
        },
        80: {
            'coordinates': np.array([5.112401, 8.084635, 0.]),
            'np': [28, 23, 79, 84, 57, 74, 98, 90],
            'px': [],
            'py': []
        },
        81: {
            'coordinates': np.array([9.152581, 9.107077, 0.]),
            'np': [59, 93, 49, 48, 66],
            'px': [],
            'py': [42]
        },
        82: {
            'coordinates': np.array([0.696605, 4.409674, 0.]),
            'np': [131, 95, 11, 10, 75, 88],
            'px': [77],
            'py': []
        },
        83: {
            'coordinates': np.array([6.7422, 4.257955, 0.]),
            'np': [92, 56, 132, 52, 36, 35],
            'px': [],
            'py': []
        },
        84: {
            'coordinates': np.array([5.312925, 7.277918, 0.]),
            'np': [80, 90, 61, 79],
            'px': [],
            'py': []
        },
        85: {
            'coordinates': np.array([9.975471, 6.983342, 0.]),
            'np': [45, 40, 41, 127, 69, 77, 99],
            'px': [],
            'py': []
        },
        86: {
            'coordinates': np.array([7.193368, 8.584019, 0.]),
            'np': [106, 68, 32, 98],
            'px': [],
            'py': []
        },
        87: {
            'coordinates': np.array([3.298118, 2.98536, 0.]),
            'np': [120, 122, 126, 13, 62],
            'px': [],
            'py': []
        },
        88: {
            'coordinates': np.array([0.869716, 6.018266, 0.]),
            'np': [110, 12, 134, 95, 82, 11],
            'px': [77, 127],
            'py': []
        },
        89: {
            'coordinates': np.array([7.882797, 2.442746, 0.]),
            'np': [133, 50, 35, 78, 52],
            'px': [],
            'py': []
        },
        90: {
            'coordinates': np.array([5.559329, 7.465366, 0.]),
            'np': [61, 58, 80, 84, 98, 105],
            'px': [],
            'py': []
        },
        91: {
            'coordinates': np.array([7.9401, 9.409426, 0.]),
            'np': [119, 53, 70, 33, 32, 106],
            'px': [],
            'py': [34]
        },
        92: {
            'coordinates': np.array([7.00556, 5.968762, 0.]),
            'np': [36, 37, 108, 51, 56, 83],
            'px': [],
            'py': []
        },
        93: {
            'coordinates': np.array([9.001977, 9.234026, 0.]),
            'np': [49, 70, 53, 59, 81],
            'px': [],
            'py': [42, 112]
        },
        94: {
            'coordinates': np.array([2.192285, 1.284963, 0.]),
            'np': [111, 9, 64, 62, 130, 6, 109],
            'px': [],
            'py': []
        },
        95: {
            'coordinates': np.array([0.431326, 4.269499, 0.]),
            'np': [88, 82, 131],
            'px': [77, 114, 72],
            'py': []
        },
        96: {
            'coordinates': np.array([9.571195, 3.161973, 0.]),
            'np': [107, 63, 43, 38, 125, 123],
            'px': [],
            'py': []
        },
        97: {
            'coordinates': np.array([1.793398, 8.352598, 0.]),
            'np': [118, 74, 7, 124, 115, 104, 65, 71, 103],
            'px': [],
            'py': []
        },
        98: {
            'coordinates': np.array([6.617838, 8.132496, 0.]),
            'np': [32, 28, 80, 90, 86, 68, 105],
            'px': [],
            'py': []
        },
        99: {
            'coordinates': np.array([9.487027, 7.283405, 0.]),
            'np': [76, 66, 41, 85, 69],
            'px': [],
            'py': []
        },
        100: {
            'coordinates': np.array([10.203263, 1.966146, 0.]),
            'np': [55, 116, 123, 47, 125, 112],
            'px': [2],
            'py': []
        },
        101: {
            'coordinates': np.array([0.702222, 2.265513, 0.]),
            'np': [67, 2, 73, 6],
            'px': [],
            'py': []
        },
        102: {
            'coordinates': np.array([3.242297, 9.989684, 0.]),
            'np': [117, 103, 128],
            'px': [],
            'py': [17]
        },
        103: {
            'coordinates': np.array([3.179244, 9.294601, 0.]),
            'np': [117, 102, 115, 128, 74, 57, 97],
            'px': [],
            'py': []
        },
        104: {
            'coordinates': np.array([1.608784, 8.957513, 0.]),
            'np': [115, 7, 97],
            'px': [],
            'py': []
        },
        105: {
            'coordinates': np.array([6.827849, 6.926306, 0.]),
            'np': [37, 51, 90, 58, 98, 68],
            'px': [],
            'py': []
        },
        106: {
            'coordinates': np.array([7.524679, 8.586315, 0.]),
            'np': [68, 54, 32, 86, 119, 91],
            'px': [],
            'py': []
        },
        107: {
            'coordinates': np.array([9.146506, 2.612103, 0.]),
            'np': [125, 63, 50, 38, 96, 116],
            'px': [],
            'py': []
        },
        108: {
            'coordinates': np.array([6.781053, 6.250603, 0.]),
            'np': [56, 92, 58, 51],
            'px': [],
            'py': []
        },
        109: {
            'coordinates': np.array([2.015902, 2.956837, 0.]),
            'np': [67, 75, 126, 62, 73, 94, 130],
            'px': [],
            'py': []
        },
        110: {
            'coordinates': np.array([2.054594, 7.224545, 0.]),
            'np': [16, 12, 118, 71, 134, 88],
            'px': [],
            'py': []
        },
        111: {
            'coordinates': np.array([2.599711, 0.335255, 0.]),
            'np': [17, 64, 94, 113, 9],
            'px': [],
            'py': [128]
        },
        112: {
            'coordinates': np.array([9.155907, 0.528067, 0.]),
            'np': [34, 42, 55, 100, 47],
            'px': [],
            'py': [70, 93]
        },
        113: {
            'coordinates': np.array([4.109585, 0.665776, 0.]),
            'np': [22, 21, 64, 17, 111],
            'px': [],
            'py': []
        },
        114: {
            'coordinates': np.array([11.06818, 4.93308, 0.]),
            'np': [123, 72, 45, 44, 77, 43],
            'px': [95],
            'py': []
        },
        115: {
            'coordinates': np.array([1.670491, 9.021622, 0.]),
            'np': [8, 7, 97, 103, 104, 128],
            'px': [],
            'py': [9]
        },
        116: {
            'coordinates': np.array([9.202781, 2.011522, 0.]),
            'np': [55, 100, 50, 107, 125, 133, 121],
            'px': [],
            'py': []
        },
        117: {
            'coordinates': np.array([3.898727, 9.53423, 0.]),
            'np': [24, 102, 57, 23, 103],
            'px': [],
            'py': [17]
        },
        118: {
            'coordinates': np.array([2.63169, 7.682275, 0.]),
            'np': [110, 16, 97, 71, 74],
            'px': [],
            'py': []
        },
        119: {
            'coordinates': np.array([8.115271, 8.716049, 0.]),
            'np': [53, 91, 59, 54, 106],
            'px': [],
            'py': []
        },
        120: {
            'coordinates': np.array([3.911436, 2.486958, 0.]),
            'np': [22, 27, 64, 62, 122, 87],
            'px': [],
            'py': []
        },
        121: {
            'coordinates': np.array([8.320459, 0.995696, 0.]),
            'np': [55, 129, 78, 116, 133],
            'px': [],
            'py': []
        },
        122: {
            'coordinates': np.array([4.078857, 3.387685, 0.]),
            'np': [87, 120, 13, 18, 132, 27],
            'px': [],
            'py': []
        },
        123: {
            'coordinates': np.array([10.670385, 3.594555, 0.]),
            'np': [125, 96, 114, 72, 100, 47, 43],
            'px': [131, 2],
            'py': []
        },
        124: {
            'coordinates': np.array([0.817694, 7.947013, 0.]),
            'np': [7, 97, 3, 134, 65],
            'px': [60, 127],
            'py': []
        },
        125: {
            'coordinates': np.array([10.134362, 2.809378, 0.]),
            'np': [123, 100, 96, 63, 107, 116],
            'px': [2],
            'py': []
        },
        126: {
            'coordinates': np.array([2.405473, 3.195753, 0.]),
            'np': [62, 87, 75, 10, 13, 109],
            'px': [],
            'py': []
        },
        127: {
            'coordinates': np.array([11.627874, 7.885213, 0.]),
            'np': [77, 85, 69, 60],
            'px': [88, 134, 124],
            'py': []
        },
        128: {
            'coordinates': np.array([3.025541, 10.099834, 0.]),
            'np': [102, 8, 115, 103],
            'px': [],
            'py': [111, 9, 17]
        },
        129: {
            'coordinates': np.array([8.003986, 0.407578, 0.]),
            'np': [55, 121, 31, 30, 78, 34],
            'px': [],
            'py': []
        },
        130: {
            'coordinates': np.array([1.514581, 1.542137, 0.]),
            'np': [94, 6, 73, 109],
            'px': [],
            'py': []
        },
        131: {
            'coordinates': np.array([0.170365, 3.874633, 0.]),
            'np': [95, 75, 82, 67],
            'px': [72, 123, 2],
            'py': []
        },
        132: {
            'coordinates': np.array([6.303232, 4.249357, 0.]),
            'np': [27, 122, 19, 18, 56, 83, 52],
            'px': [],
            'py': []
        },
        133: {
            'coordinates': np.array([8.219924, 1.555487, 0.]),
            'np': [121, 78, 89, 116, 50],
            'px': [],
            'py': []
        },
        134: {
            'coordinates': np.array([1.106431, 7.482676, 0.]),
            'np': [124, 71, 110, 65, 88],
            'px': [127],
            'py': [
            ]}
    }

    s.compute_info()
    info = s.load_info()

    import os
    import glob

    for match in glob.glob(s.temp_prefix + '*'):
        os.remove(match)

    assert(all([
        (info[i]['coordinates'] == info_ref[i]['coordinates']).all()
        for i in info_ref
    ]))
    assert(all([
        (info[i]['coordinates'] == info_ref[i]['coordinates']).all()
        for i in info
    ]))
    assert(all([info[i]['np'] == info_ref[i]['np'] for i in info_ref]))
    assert(all([info[i]['np'] == info_ref[i]['np'] for i in info]))
    assert(all([info[i]['px'] == info_ref[i]['px'] for i in info_ref]))
    assert(all([info[i]['px'] == info_ref[i]['px'] for i in info]))
    assert(all([info[i]['py'] == info_ref[i]['py'] for i in info_ref]))
    assert(all([info[i]['py'] == info_ref[i]['py'] for i in info]))


def test_lattice_name_defaults():
    s1 = Sample(2, 2, 2)
    s2 = Sample(2.0, 2.0, 2.0)

    assert(s1.lattice_name() == 'square hex r2 d2 l2 a1.0')
    assert(s2.lattice_name() == 'square hex r2.0 d2.0 l2.0 a1.0')


def test_xml_lattice_defaults():
    import lxml.etree as ETree

    s1 = Sample(2, 2, 2)
    s2 = Sample(2.0, 2.0, 2.0)

    lattice1 = ETree.XML("""\
<LATTICE dimension="2" name="square hex r2 d2 l2 a1.0">
  <BASIS>
    <VECTOR>12.000000 0</VECTOR>
    <VECTOR>0 10.392305</VECTOR>
  </BASIS>
</LATTICE>\
""")

    lattice2 = ETree.XML("""\
<LATTICE dimension="2" name="square hex r2.0 d2.0 l2.0 a1.0">
  <BASIS>
    <VECTOR>12.000000 0</VECTOR>
    <VECTOR>0 10.392305</VECTOR>
  </BASIS>
</LATTICE>\
""")
    assert(ETree.dump(s1.xml_lattice()) == ETree.dump(lattice1))
    assert(ETree.dump(s2.xml_lattice()) == ETree.dump(lattice2))


def test_finite_lattice_name_defaults():
    s1 = Sample(2, 2, 2)
    s2 = Sample(2.0, 2.0, 2.0)

    assert(s1.finite_lattice_name() == 'single square hex r2 d2 l2 a1.0')
    assert(s2.finite_lattice_name() == 'single square hex r2.0 d2.0 l2.0 a1.0')


def test_xml_finite_lattice_defaults():
    import lxml.etree as ETree

    s = Sample(2, 2, 2)

    finite_lattice = ETree.XML("""\
<FINITELATTICE dimension="2" name="single square hex r2 d2 l2 a1.0">
  <LATTICE ref="square hex r2 d2 l2 a1.0"/>
  <EXTENT dimension="1" size="1"/>
  <EXTENT dimension="2" size="1"/>
  <BOUNDARY type="periodic"/>
</FINITELATTICE>\
""")

    assert(ETree.dump(s.xml_finite_lattice()) == ETree.dump(finite_lattice))


def test_xml_finite_lattice_no_ref():
    import lxml.etree as ETree

    s = Sample(2, 2, 2)

    ref_finite_lattice = ETree.XML("""\
<FINITELATTICE dimension="2" name="single square hex r2 d2 l2 a1.0">
  <LATTICE dimension="2" name="square hex r2 d2 l2 a1.0">
    <BASIS>
      <VECTOR>12.000000 0</VECTOR>
      <VECTOR>0 10.392305</VECTOR>
    </BASIS>
  </LATTICE>
  <EXTENT dimension="1" size="1"/>
  <EXTENT dimension="2" size="1"/>
  <BOUNDARY type="periodic"/>
</FINITELATTICE>\
""")

    finite_lattice = s.xml_finite_lattice(ref_lattice=False)

    assert(ETree.dump(ref_finite_lattice) == ETree.dump(finite_lattice))
