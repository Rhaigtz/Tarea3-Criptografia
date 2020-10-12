from oscrypto import symmetric
import codecs



encrypted = symmetric.rc4_encrypt(b'key 123', b'text')

print(codecs.encode(encrypted, 'hex'))


decripted = symmetric.rc4_decrypt(b'key 123', encrypted)

print(decripted.hex())