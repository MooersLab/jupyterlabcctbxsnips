Iobs = miller_arrays[0]
i_plus, i_minus = Iobs.hemispheres_acentrics()
ipd = i_plus.data()
ip=list(ipd)
imd = i_minus.data()
im = list(imd)
len(im)
Iobs.show_summary()
print(Iobs.info())
print(Iobs.observation_type())
$0
# Description:  Unpack into I(+) and I(-) for a specified Miller array. 
# Source:  NA

Iobs = miller_arrays[0]
i_plus, i_minus = Iobs.hemispheres_acentrics()
ipd = i_plus.data()
ip=list(ipd)
imd = i_minus.data()
im = list(imd)
len(im)
Iobs.show_summary()
print(Iobs.info())
print(Iobs.observation_type())

# Description:  Unpack into I(+) and I(-) for a specified Miller array. 
# Source:  NA

