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
    assert(False)


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
