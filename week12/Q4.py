import hashlib
def hashing_func(key):
    result = hashlib.md5(key.encode())
    return result    

def insert(hash_table, key, value):    #If the key is already present in the hash table, then we update its value with the new one.  
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
        
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))

def get(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        print (bucket[i])
    else:
        print ("No items with this index")


hash_table = [[] for _ in range(10)]
print (hash_table)  



insert(hash_table, 10, 'Nepal')
print (hash_table)

delete(hash_table,10)
print(hash_table)
