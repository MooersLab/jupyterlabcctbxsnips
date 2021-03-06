from iotbx import mtz
mtz_obj = mtz.object(file_name="3nd4.mtz")
miller_arrays = mtz_obj.as_miller_arrays()
miller_array_truncated = miller_arrays[0].resolution_filter(d_min=2, d_max=5)
print(miller_array_truncated)
miller_array_truncated.show_summary()
