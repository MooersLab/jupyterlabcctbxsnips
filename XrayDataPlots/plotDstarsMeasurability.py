from iotbx.reflection_file_reader import any_reflection_file
hkl_file = any_reflection_file("3hz7.mtz")
miller_arrays = hkl_file.as_miller_arrays(merge_equivalents=False)

Iobs = miller_arrays[1]
# Set up the bins
n_bins = 50
binner = Iobs.setup_binner(n_bins=n_bins)
# binner.show_summary()
used = list(binner.range_used())
selections = [binner.selection(i) for i in used]

# make d_centers for the x-axis
d_star_power = 1.618034
centers = binner.bin_centers(d_star_power)
d_centers = list(centers**(-1 / d_star_power))

# make list of the measurabilities by resolution bin
meas = [Iobs.select(sel).measurability() for sel in selections]

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["savefig.dpi"] = 600
mpl.rcParams["figure.dpi"] = 600

fig, ax = plt.subplots(figsize=[3.25, 2.])
ax.scatter(d_centers,lnmeans,c="k",alpha=0.3,s=5.5)

ax.set_xlim(8, 1.5) # decreasing time
ax.set_xlabel(r"$d^*$ in $\AA$",fontsize=12)
ax.set_ylabel("ln(I)",fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.grid(False)
plt.savefig("3hz7measureability.pdf",bbox_inches="tight")
plt.show()
