import hashlib

# {'shake_128', 'md5', 'shake256', 'md5-sha1', 'sha512-256', 
# 'blake2s', 'sha512-224', 'sha3_512', 'sha3-256', 'sha384', 
# 'sha3-224', 'sha256', 'sha3_256', 'whirlpool', 'sha3_384', 
# 'sha1', 'shake128', 'sha3-512', 'md4', 'blake2b512', 'sha512', 
# 'sha224', 'sm3', 'ripemd160', 'blake2s256', 'sha3_224', 
# 'sha3-384', 'shake_256', 'blake2b'}
def create_hash_password(string, hash='sha256'):
    string = str(string)
    if string != None and string != '':
        if hash != None:
            if hash == 'getAll':
                return str(hashlib.algorithms_guaranteed) + "\n\n" + str(hashlib.algorithms_available)
            else:
                hash = hashlib.new(hash)
                hash.update(string.encode('utf-8'))
                return hash.hexdigest()

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    print (create_hash_password('test', hash='sha256'))
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")