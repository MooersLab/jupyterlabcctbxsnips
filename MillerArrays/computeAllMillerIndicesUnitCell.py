from cctbx import crystal
from cctbx import miller

ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol="P4",
        unit_cell=(150.8,150.8,250.4,90.0,90.0,90.0)),
    anomalous_flag=False,
    d_min=1.4)
msu = ms.map_to_asu()
[print(hkl) for hkl in msu.indices()]
print(msu.show_comprehensive_summary())
