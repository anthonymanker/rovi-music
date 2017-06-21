import time
import hashlib

def computesig(apikey, secretkey):

	unixtime = time.time()
	concat = str(apikey) + str(secretkey) + str(unixtime)
	m = hashlib.md5()
	m.update(concat.encode('utf-8'))
	return m.hexdigest()