""" 
This script reads in a phenix.refine mtz file.
It plots the R-factor by resolution bin.
The plots are made with matplotlib using miller arrays.
It also plots the correlation coefficients.
The plots were made with matplotlib.

This script was adapted from an example script in iotbx:  

Source:  https://github.com/cctbx/cctbx_project/blob/master/
iotbx/examples/recalculate_phenix_refine_r_factors.py
"""


# get_ipython().run_line_magic('matplotlib', 'inline')

from __future__ import absolute_import, division, print_function
from iotbx.reflection_file_utils import get_r_free_flags_scores
from iotbx.file_reader import any_file
import matplotlib
import matplotlib.pyplot as plt



def compute_r_factors(fobs, fmodel, flags):
  fmodel, fobs = fmodel.common_sets(other=fobs)
  fmodel, flags = fmodel.common_sets(other=flags)
  fc_work = fmodel.select(~(flags.data()))
  fo_work = fobs.select(~(flags.data()))
  fc_test = fmodel.select(flags.data())
  fo_test = fobs.select(flags.data())
  r_work = fo_work.r1_factor(fc_work)
  r_free = fo_test.r1_factor(fc_test)
  
  print("r_work = %.4f" % r_work)
  print("r_free = %.4f" % r_free)
  print("")

  binner = flags.setup_binner(n_bins=20)
  d_star_power = 1.618034
  centers = binner.bin_centers(d_star_power)
  d_centers = list(centers**(-1 / d_star_power))
#   for i in d_centers:
#     print(i)
    
  fo_work.use_binning_of(flags)
  fc_work.use_binner_of(fo_work)
  fo_test.use_binning_of(fo_work)
  fc_test.use_binning_of(fo_work)

  r_work_list = []
  r_free_list = []
  cc_work_list = []
  cc_free_list = []
  for i_bin in fo_work.binner().range_all():
    sel_work = fo_work.binner().selection(i_bin)
    sel_test = fo_test.binner().selection(i_bin)
    fo_work_bin = fo_work.select(sel_work)
    fc_work_bin = fc_work.select(sel_work)
    fo_test_bin = fo_test.select(sel_test)
    fc_test_bin = fc_test.select(sel_test)
    if fc_test_bin.size() == 0 : continue
        
    r_work_bin = fo_work_bin.r1_factor(other=fc_work_bin,
      assume_index_matching=True)
    r_work_list.append(r_work_bin)
    
    r_free_bin = fo_test_bin.r1_factor(other=fc_test_bin,
      assume_index_matching=True)
    r_free_list.append(r_free_bin)
    
    cc_work_bin = fo_work_bin.correlation(fc_work_bin).coefficient()
    cc_work_list.append(cc_work_bin)
    
    cc_free_bin = fo_test_bin.correlation(fc_test_bin).coefficient()
    cc_free_list.append(cc_free_bin)
    
    legend = flags.binner().bin_legend(i_bin, show_counts=False)
    print("%s  %8d %8d  %.4f %.4f  %.3f %.3f" % (legend, fo_work_bin.size(),
      fo_test_bin.size(), r_work_bin, r_free_bin, cc_work_bin, cc_free_bin))
    
  return d_centers, r_work_list, r_free_list, cc_work_list, cc_free_list


def plot_r_factors(d_centers, r_work_list, r_free_list):
  plt.scatter(d_centers, r_work_list, label=r"$\mathit{R_{work$")
  plt.scatter(d_centers, r_free_list, label=r"$\mathit{R_{free$")
  plt.xlabel(r"Resolution ($\mathrm{\AA$)")
  plt.ylabel(r"R-factor (%)")
  plt.legend(loc="upper right")
  plt.savefig("Rs.pdf")
  plt.close()


def plot_cc(d_centers, cc_work_list, cc_free_list):
  plt.scatter(d_centers, cc_work_list, label=r"$\mathit{CC_{work$")
  plt.scatter(d_centers, cc_free_list, label=r"$\mathit{CC_{free$")
  plt.xlabel(r"Resolution ($\mathrm{\AA$)")
  plt.ylabel(r"Correlation Coefficeint Fo vs Fc (%)")
  plt.legend(loc="lower right")
  plt.savefig("CCs.pdf")


def run(input_mtz):
  mtz_in = any_file(input_mtz)
  ma = mtz_in.file_server.miller_arrays
  flags = fmodel = fobs = None
  # select the output arrays from phenix.refine.  This could easily be modified
  # to handle MTZ files from other programs.
  for array in ma :
    labels = array.info().label_string()
    if labels.startswith("R-free-flags"):
      flags = array
    elif labels.startswith("F-model"):
      fmodel = abs(array)
    elif labels.startswith("F-obs-filtered"):
      fobs = array
  if (None in [flags, fobs, fmodel]):
    raise RuntimeError("Not a valid phenix.refine output file")
  scores = get_r_free_flags_scores([flags], None)
  test_flag_value = scores.test_flag_values[0]
  flags = flags.customized_copy(data=flags.data()==test_flag_value)

  (d_centers, 
   r_work_list, 
   r_free_list, 
   cc_work_list, 
   cc_free_list) = compute_r_factors(fobs, fmodel, flags)
  plot_r_factors(d_centers, r_work_list, r_free_list)
  plot_cc(d_centers, cc_work_list, cc_free_list)


if (__name__ == "__main__"):
  run(input_mtz="28molrepEdited_5_refine_001.mtz")
# Description:  Example of computing Fcalcs and then plotting them by resolution bin. This script uses miller arrays and binner.
# Source:  NA

""" 
This script reads in a phenix.refine mtz file.
It plots the R-factor by resolution bin.
The plots are made with matplotlib using miller arrays.
It also plots the correlation coefficients.
The plots were made with matplotlib.

This script was adapted from an example script in iotbx:  

Source:  https://github.com/cctbx/cctbx_project/blob/master/
iotbx/examples/recalculate_phenix_refine_r_factors.py
"""


# get_ipython().run_line_magic('matplotlib', 'inline')

from __future__ import absolute_import, division, print_function
from iotbx.reflection_file_utils import get_r_free_flags_scores
from iotbx.file_reader import any_file
import matplotlib
import matplotlib.pyplot as plt



def compute_r_factors(fobs, fmodel, flags):
  fmodel, fobs = fmodel.common_sets(other=fobs)
  fmodel, flags = fmodel.common_sets(other=flags)
  fc_work = fmodel.select(~(flags.data()))
  fo_work = fobs.select(~(flags.data()))
  fc_test = fmodel.select(flags.data())
  fo_test = fobs.select(flags.data())
  r_work = fo_work.r1_factor(fc_work)
  r_free = fo_test.r1_factor(fc_test)
  
  print("r_work = %.4f" % r_work)
  print("r_free = %.4f" % r_free)
  print("")

  binner = flags.setup_binner(n_bins=20)
  d_star_power = 1.618034
  centers = binner.bin_centers(d_star_power)
  d_centers = list(centers**(-1 / d_star_power))
#   for i in d_centers:
#     print(i)
    
  fo_work.use_binning_of(flags)
  fc_work.use_binner_of(fo_work)
  fo_test.use_binning_of(fo_work)
  fc_test.use_binning_of(fo_work)

  r_work_list = []
  r_free_list = []
  cc_work_list = []
  cc_free_list = []
  for i_bin in fo_work.binner().range_all():
    sel_work = fo_work.binner().selection(i_bin)
    sel_test = fo_test.binner().selection(i_bin)
    fo_work_bin = fo_work.select(sel_work)
    fc_work_bin = fc_work.select(sel_work)
    fo_test_bin = fo_test.select(sel_test)
    fc_test_bin = fc_test.select(sel_test)
    if fc_test_bin.size() == 0 : continue
        
    r_work_bin = fo_work_bin.r1_factor(other=fc_work_bin,
      assume_index_matching=True)
    r_work_list.append(r_work_bin)
    
    r_free_bin = fo_test_bin.r1_factor(other=fc_test_bin,
      assume_index_matching=True)
    r_free_list.append(r_free_bin)
    
    cc_work_bin = fo_work_bin.correlation(fc_work_bin).coefficient()
    cc_work_list.append(cc_work_bin)
    
    cc_free_bin = fo_test_bin.correlation(fc_test_bin).coefficient()
    cc_free_list.append(cc_free_bin)
    
    legend = flags.binner().bin_legend(i_bin, show_counts=False)
    print("%s  %8d %8d  %.4f %.4f  %.3f %.3f" % (legend, fo_work_bin.size(),
      fo_test_bin.size(), r_work_bin, r_free_bin, cc_work_bin, cc_free_bin))
    
  return d_centers, r_work_list, r_free_list, cc_work_list, cc_free_list


def plot_r_factors(d_centers, r_work_list, r_free_list):
  plt.scatter(d_centers, r_work_list, label=r"$\mathit{R_{work$")
  plt.scatter(d_centers, r_free_list, label=r"$\mathit{R_{free$")
  plt.xlabel(r"Resolution ($\mathrm{\AA$)")
  plt.ylabel(r"R-factor (%)")
  plt.legend(loc="upper right")
  plt.savefig("Rs.pdf")
  plt.close()


def plot_cc(d_centers, cc_work_list, cc_free_list):
  plt.scatter(d_centers, cc_work_list, label=r"$\mathit{CC_{work$")
  plt.scatter(d_centers, cc_free_list, label=r"$\mathit{CC_{free$")
  plt.xlabel(r"Resolution ($\mathrm{\AA$)")
  plt.ylabel(r"Correlation Coefficeint Fo vs Fc (%)")
  plt.legend(loc="lower right")
  plt.savefig("CCs.pdf")


def run(input_mtz):
  mtz_in = any_file(input_mtz)
  ma = mtz_in.file_server.miller_arrays
  flags = fmodel = fobs = None
  # select the output arrays from phenix.refine.  This could easily be modified
  # to handle MTZ files from other programs.
  for array in ma :
    labels = array.info().label_string()
    if labels.startswith("R-free-flags"):
      flags = array
    elif labels.startswith("F-model"):
      fmodel = abs(array)
    elif labels.startswith("F-obs-filtered"):
      fobs = array
  if (None in [flags, fobs, fmodel]):
    raise RuntimeError("Not a valid phenix.refine output file")
  scores = get_r_free_flags_scores([flags], None)
  test_flag_value = scores.test_flag_values[0]
  flags = flags.customized_copy(data=flags.data()==test_flag_value)

  (d_centers, 
   r_work_list, 
   r_free_list, 
   cc_work_list, 
   cc_free_list) = compute_r_factors(fobs, fmodel, flags)
  plot_r_factors(d_centers, r_work_list, r_free_list)
  plot_cc(d_centers, cc_work_list, cc_free_list)


if (__name__ == "__main__"):
  run(input_mtz="28molrepEdited_5_refine_001.mtz")
# Description:  Example of computing Fcalcs and then plotting them by resolution bin. This script uses miller arrays and binner.
# Source:  NA

