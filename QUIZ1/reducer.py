import sys
import numpy as np


#I read numpy returns the population and not sample std dev, but from what I saw on the link 
#it was returning the population std dev, also, so I used that.
#if we wanted smaple, could add ddof=1 to the np.std() call
std = lambda x: np.std(np.array(x))

curSpecies = ""
(n, speciesWeights) = (0,[])

for line in sys.stdin:
	(k,w) = line.split('|')
	
	#data was cleaned in mapper, so confident only data that can be converted from string to float reaches reducer
	w = [ float(w) ]


	if k != curSpecies:
		#1.Before starting the new group (species), get the std for the curSpecies

		if curSpecies:			#First group curSpecies is ""
			print(curSpecies,std(speciesWeights))

		#2. Now start a new group(species), reset values
		(curSpecies,n,speciesWeights) = (k,1,w)
	else:
		#same group(species), increment n and groupS
		n += 1
		speciesWeights += w

#last group finished - get those results too
print(curSpecies,std(speciesWeights))
		
		

