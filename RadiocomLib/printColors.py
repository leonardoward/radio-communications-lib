class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printHeader (text):
	return print(bcolors.HEADER+text+bcolors.ENDC)

def printSubHeader (text):
    return print(bcolors.OKBLUE+text+bcolors.ENDC)

def printOK (text):
	return print(bcolors.OKGREENK+text+bcolors.ENDC)

def printWarning (text):
	return print(bcolors.WARNING+text+bcolors.ENDC)

def printFail (text):
	return print(bcolors.FAIL+text+bcolors.ENDC)

def printBold (text):
	return print(bcolors.BOLD+text+bcolors.ENDC)

def printUnderline (text):
	return print(bcolors.UNDERLINE+text+bcolors.ENDC)


