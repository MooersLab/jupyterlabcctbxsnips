from iotbx.pdb.fetch import get_pdb
import sys
get_pdb(id="3nd4",data_type="xray", mirror="rcsb", format="cif", log=sys.stdout)
