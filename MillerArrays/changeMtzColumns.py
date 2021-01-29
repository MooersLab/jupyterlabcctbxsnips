from iotbx.reflection_file_reader import any_reflection_file
hkl_in = any_reflection_file("/Users/blaine/manuscripts/RETkinaseLoxo/ret_blu.mtz")

miller_arrays = hkl_in.as_miller_arrays()

i_obs =  miller_arrays[3]
r_free_flags = miller_arrays[0]
f_obs = i_obs.f_sq_as_f()

mtz_dataset = i_obs.as_mtz_dataset(column_root_label="I")
mtz_dataset.add_miller_array(f_obs, column_root_label="F")
mtz_dataset.add_miller_array(r_free_flags,column_root_label="FreeR_flag")
mtz_dataset.mtz_object().write("loxodata.mtz")
