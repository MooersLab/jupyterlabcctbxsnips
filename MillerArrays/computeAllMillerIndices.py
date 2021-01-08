from cctbx import miller

def generate_reflection_indices(uc, dmin):
    maxh, maxk, maxl = uc.max_miller_indices(dmin)

    indices = []

    for h in range(-maxh, maxh + 1):
        for k in range(-maxk, maxk + 1):
            for l in range(-maxl, maxl + 1):
                if h == 0 and k == 0 and l == 0:
                    continue
                if uc.d((h, k, l)) < dmin:
                    continue
        indices.append((h, k, l))
    return indices
    
uc=(5.4307,5.4307,5.4307,90.00,90.0,90.00)
dmin=1.0
$0
# Description:  Compute all possible Miller indices.
# Source:  NA

from cctbx import miller

def generate_reflection_indices(uc, dmin):
    maxh, maxk, maxl = uc.max_miller_indices(dmin)

    indices = []

    for h in range(-maxh, maxh + 1):
        for k in range(-maxk, maxk + 1):
            for l in range(-maxl, maxl + 1):
                if h == 0 and k == 0 and l == 0:
                    continue
                if uc.d((h, k, l)) < dmin:
                    continue
        indices.append((h, k, l))
    return indices
    
uc=(5.4307,5.4307,5.4307,90.00,90.0,90.00)
dmin=1.0

# Description:  Compute all possible Miller indices.
# Source:  NA

