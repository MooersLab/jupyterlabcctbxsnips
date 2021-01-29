from iotbx import mtz
mtz_obj = mtz.object(file_name="2V89.mtz")
miller_arrays = mtz_obj.as_miller_arrays()
for miller_array in miller_arrays:
    miller_array_truncated = miller_array.resolution_filter(d_min=2, d_max=5)
print(miller_array_truncated)
