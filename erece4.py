from Crypto.Cipher import ARC4
import codecs

key = b'key 123'
cipher = ARC4.new(key)
msg = cipher.encrypt(b'text')

print(codecs.encode(msg, 'hex'))
