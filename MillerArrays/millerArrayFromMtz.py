from iotbx import mtz
mtz_obj = mtz.object(file_name="3nd4.mtz")
miller_arrays = mtz_obj.as_miller_arrays()
