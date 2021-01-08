"""
from iotbx.pdb.fetch import get_pdb
import sys
get_pdb(id="${1:3nd4}",data_type="pdb", mirror="rcsb", format="pdb", log=sys.stdout)
"""
from iotbx.pdb.fetch import get_pdb
import sys
get_pdb(id="3nd4",data_type="pdb", mirror="rcsb", format="pdb", log=sys.stdout)

# Description:  Fetch pdb file from RCSB in PDB format.
# Source:  NA

