import sys
import re

birds = {}

for line in sys.stdin:
	try:
		words = line.split()

		#lowercase all breeds in case of mixed cases in data
		#assumption - punction (apostrophes, hyphens, etc) are correct in data
		#(other option would have been to remove them when reading input)

		words = [w.strip().lower() for w in words]

		#also don't bother sending bad data in the weight field onto the reducer - it will be caught also
		words[-1] = float(words[-1])

		out=" ".join(words[:-1]) + "|" + str(words[-1])
		print(out)
	except:
		#skip exceptions caused by blank lines or lines w/out an appropriate weight value 
		continue
