import cPickle as pickle
import requests
import rsa

with open('./privatekey.key.pkl') as f :
	key = pickle.load(f)

r = requests.get('https://github.com/agnussmcferguss/pi-anywhere/blob/master/cript.ip?raw=true')
message = r.content[:-1]

print rsa.decrypt(message, key)

