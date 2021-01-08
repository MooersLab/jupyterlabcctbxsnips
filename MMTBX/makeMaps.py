from mmtbx.maps.utils import create_map_from_pdb_and_mtz
"""The phenix.maps commandline tool is the recommended approach."""
id="3nd4"
create_map_from_pdb_and_mtz(
          pdb_file="%s.pdb" % id,
          mtz_file="%s.mtz" % id,
          output_file="%s_maps.mtz" % id,
          fill=False,
          out=None,
          llg_map=False,
          remove_unknown_scatterering_type=True,
          assume_pdb_data=False)
$0
# Description:  Read in mtz and pdb file and write map coefficients to a separate mtz file.
# Source:  NA

from mmtbx.maps.utils import create_map_from_pdb_and_mtz
"""The phenix.maps commandline tool is the recommended approach."""
id="3nd4"
create_map_from_pdb_and_mtz(
          pdb_file="%s.pdb" % id,
          mtz_file="%s.mtz" % id,
          output_file="%s_maps.mtz" % id,
          fill=False,
          out=None,
          llg_map=False,
          remove_unknown_scatterering_type=True,
          assume_pdb_data=False)

# Description:  Read in mtz and pdb file and write map coefficients to a separate mtz file.
# Source:  NA

