import hashlib

result = hashlib.md5(b'1abcd1234')
print(result.hexdigest())