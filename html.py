from arc4 import ARC4
from reece4 import Text
from rece4 import encrypt, decrypt

encrypted = encrypt('key', 'text')

print(encrypted)
decrypted = decrypt('key', encrypted)


print(decrypted)
