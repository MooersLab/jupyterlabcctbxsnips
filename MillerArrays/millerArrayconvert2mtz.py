# Convert the miller array into a mtz_dataset and write out as a mtz file.
mtz_dataset = Iobs.as_mtz_dataset(column_root_label="I")
mtz_dataset.mtz_object().write("3hz7intensities.mtz")
