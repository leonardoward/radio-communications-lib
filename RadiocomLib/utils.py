
def dBm2dB (dBm):
	return dBm + 3

def dB2dBm (dB): 
	return dB - 3

def m2Km(values):
	if(isinstance(values, float) or isinstance(values, int)):
		return values/1000
	distance_ = []
	# convert from m to Km
	for i in range(0, len(values)):
		distance_.append(values[i]/1000)

	return distance_

def Km2m(values):
	if(isinstance(values, float) or isinstance(values, int)):
		return values*1000
	distance_ = []
	# convert from Km to m
	for i in range(0, len(values)):
		distance_.append(values[i]*1000)

	return distance_