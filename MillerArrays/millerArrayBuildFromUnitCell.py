from cctbx import miller
import cctbx
from cctbx import crystal

ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol='Fd-3m',
        unit_cell=(5.4307,5.4307,5.4307,90.00,90.0,90.00)),
    anomalous_flag=True,
    d_min=0.4)

[print(hkl) for hkl in ms.indices()]
$0
# Description:  Peter Zwart's code for generating the indices for unit cell of given symmetry and dimensions. 
# Source:  NA

from cctbx import miller
import cctbx
from cctbx import crystal

ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol='Fd-3m',
        unit_cell=(5.4307,5.4307,5.4307,90.00,90.0,90.00)),
    anomalous_flag=True,
    d_min=0.4)

[print(hkl) for hkl in ms.indices()]

# Description:  Peter Zwart's code for generating the indices for unit cell of given symmetry and dimensions. 
# Source:  NA

