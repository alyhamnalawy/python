import hashlib

def get_hash(message):
    message_bytes = message.encode()
    hash_obj = hashlib.sha256(message_bytes)  
    hash = hash_obj.hexdigest()   
    return hash
text = input("enter some text:")
hash = get_hash(text)
print("the SHA256 is:")
print(hash)