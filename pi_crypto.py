# Encryption stub - possibly unnecessary duplication
import rsa
import cPickle as pickle
import sys

def create_key_pair(size=2048) :
	pubkey, privkey = rsa.newkeys(size)
	return pubkey, privkey

def encrypt_message(message, pubkey) :
	return rsa.encrypt(message, pubkey)

def decrypt_message(message, privkey) :
	return rsa.decrypt(message, privkey)

if __name__ == '__main__' :
	message = sys.argv[1]
	with open('./pubkey.key.pkl') as f :
		pubkey = pickle.load(f)
	print encrypt_message(message, pubkey)