from iotbx.reflection_file_reader import any_reflection_file
hkl_file = any_reflection_file('3hz7.mtz')
miller_arrays = hkl_file.as_miller_arrays(merge_equivalents=False)
$0
# Description:  Read a mtz file into a miller array.
# Source:  NA

from iotbx.reflection_file_reader import any_reflection_file
hkl_file = any_reflection_file('3hz7.mtz')
miller_arrays = hkl_file.as_miller_arrays(merge_equivalents=False)

# Description:  Read a mtz file into a miller array.
# Source:  NA

