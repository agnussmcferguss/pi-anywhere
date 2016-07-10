# Encryption stub - possibly unnecessary duplication

import rsa

def create_key_pair(size=2048) :
	pubkey, privkey = rsa.newkeys(size)
	return pubkey, privkey

def encrypt_message(message, pubkey) :
	return rsa.encrypt(message, pubkey)

def decrypt_message(message, privkey) :
	return rsa.decrypt(message, privkey)
