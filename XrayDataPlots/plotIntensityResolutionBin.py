from iotbx.file_reader import any_file
import matplotlib.pyplot as plt

f = any_file("/Users/blaine/manuscripts/RETkinaseLoxo/ret_blu.mtz")

print(f.file_type)
f.show_summary()
miller_arrays = f.file_server.miller_arrays
iobs =  miller_arrays[3]
flags = miller_arrays[0]
iobs, flags = iobs.common_sets(other=flags)
iobsData = iobs.data()
list(iobsData[100:110])
iobs.show_comprehensive_summary()
# iobs.binner()
n_bins = 20
binner = iobs.setup_binner(n_bins=n_bins)
binner.show_summary()

used = list(binner.range_used())
selections = [binner.selection(i) for i in used]
means = [iobs.select(sel).mean() for sel in selections]

from math import log
lnmeans = [log(y) for y in means]

d_star_power = 1.618034
centers = binner.bin_centers(d_star_power)
d_centers = list(centers**(-1 / d_star_power))
d_centers

# plt.ylabel('Natural log of the amplitudes squared')
# plt.xlabel(r'$\textrm{d^*$ in $\textrm{\AA$')
# ax.set_xlim(35, 1.5)
# plt.scatter(d_centers,lnmeanss)

fig, ax = plt.subplots()
ax.scatter(d_centers,lnmeans)
ax.set_xlim(8, 1.5)  # decreasing
ax.set_xlabel(r'$d^*$ in $\AA$')
ax.set_ylabel('Natural log of the intensities')
ax.grid(False)
plt.savefig("iobsvsdstar.pdf")
$0
# Description:  Miller arrays to plot of bin mean intensity over dstar
# Source:  NA

from iotbx.file_reader import any_file
import matplotlib.pyplot as plt

f = any_file("/Users/blaine/manuscripts/RETkinaseLoxo/ret_blu.mtz")

print(f.file_type)
f.show_summary()
miller_arrays = f.file_server.miller_arrays
iobs =  miller_arrays[3]
flags = miller_arrays[0]
iobs, flags = iobs.common_sets(other=flags)
iobsData = iobs.data()
list(iobsData[100:110])
iobs.show_comprehensive_summary()
# iobs.binner()
n_bins = 20
binner = iobs.setup_binner(n_bins=n_bins)
binner.show_summary()

used = list(binner.range_used())
selections = [binner.selection(i) for i in used]
means = [iobs.select(sel).mean() for sel in selections]

from math import log
lnmeans = [log(y) for y in means]

d_star_power = 1.618034
centers = binner.bin_centers(d_star_power)
d_centers = list(centers**(-1 / d_star_power))
d_centers

# plt.ylabel('Natural log of the amplitudes squared')
# plt.xlabel(r'$\textrm{d^*$ in $\textrm{\AA$')
# ax.set_xlim(35, 1.5)
# plt.scatter(d_centers,lnmeanss)

fig, ax = plt.subplots()
ax.scatter(d_centers,lnmeans)
ax.set_xlim(8, 1.5)  # decreasing
ax.set_xlabel(r'$d^*$ in $\AA$')
ax.set_ylabel('Natural log of the intensities')
ax.grid(False)
plt.savefig("iobsvsdstar.pdf")

# Description:  Miller arrays to plot of bin mean intensity over dstar
# Source:  NA

