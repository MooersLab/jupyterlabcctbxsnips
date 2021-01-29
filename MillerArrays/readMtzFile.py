from iotbx.file_reader import any_file
mtz_in = any_file("data.mtz", force_type="mtz")
miller_arrays = mtz_in.file_server.miller_arrays
