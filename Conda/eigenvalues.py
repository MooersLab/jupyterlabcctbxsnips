from scitbx.array_family import flex;
from scitbx.linalg import eigensystem;
m = flex.double(($1:-2, -4, 2, -2, 1, 2, 4, 2, 5));
m.reshape(flex.grid(3,3));
es = eigensystem.real_symmetric(m);
list(es.values());
list(es.vectors());
