from iotbx import mtz
mtz_obj = mtz.object(file_name="/Users/blaine/3nd4.mtz")
# Only works with mtz.object. Does not work if mtz is read in with iotbx.file_reader.
miller_arrays_dict = mtz_obj.as_miller_arrays_dict()
[print(f"Column label: {key[2]")  for key in miller_arrays_dict.keys()]
$0
# Description:  Print the column labels of Miller dictionary.
# Source:  NA

from iotbx import mtz
mtz_obj = mtz.object(file_name="/Users/blaine/3nd4.mtz")
# Only works with mtz.object. Does not work if mtz is read in with iotbx.file_reader.
miller_arrays_dict = mtz_obj.as_miller_arrays_dict()
[print(f"Column label: {key[2]")  for key in miller_arrays_dict.keys()]

# Description:  Print the column labels of Miller dictionary.
# Source:  NA

