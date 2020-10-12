#!/usr/bin/env python

"""a simple encryption script using RC4"""

import sys


class Text(object):

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return '%s' % self.filename

    def text_to_bytes(self):

        byteList = []

        f = open(self.filename, 'r')
        s = f.read()
        f.close()

        # on Windows, default coding for Chinese is GBK
        # s = s.decode('gbk').encode('utf-8')
        for byte in s:
            byteList.append(ord(byte))

        return byteList

    def hex_to_bytes(self):

        byteList = []
        f = open(self.filename, 'r')

        hexStr = f.read()
        for i in range(0, len(hexStr), 2):
            byte = hexStr[i:i+2]
            byteList.append(int('0X' + byte, 16))

        f.close()
        return byteList

    def bytes_to_text(self, ByteList):

        s = ''
        for byte in ByteList:
            s += chr(byte)

        f = open(self.filename, 'w')

        # on Windows, default coding for Chinese is GBK
        # s = s.decode('utf-8').encode('gbk')
        f.write(s)

        f.close()

    def bytes_to_hex(self, ByteList):

        f = open(self.filename, 'w')

        for byte in ByteList:
            hexStr = '0' + hex(byte)[2:]
            f.write(hexStr[-2:].upper())

        f.close()

    def encrypt(self, Key):

        PlainBytes = self.text_to_bytes()
        KeyBytes = Key.text_to_bytes()
        KeystreamBytes, CipherBytes = crypt(PlainBytes, KeyBytes)
        Keystream = Text('keystream.txt')
        Cipher = Text('hex.txt')
        Keystream.bytes_to_hex(KeystreamBytes)
        Cipher.bytes_to_hex(CipherBytes)

    def decrypt(self, Key):

        CipherBytes = self.hex_to_bytes()
        KeyBytes = Key.text_to_bytes()
        KeystreamBytes, PlainBytes = crypt(CipherBytes, KeyBytes)
        Plain = Text('plain.txt')
        Keystream = Text('keystream.txt')
        Keystream.bytes_to_hex(KeystreamBytes)
        Plain.bytes_to_text(PlainBytes)


def crypt(PlainBytes, KeyBytes):

    keystreamList = []
    cipherList = []

    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + KeyBytes[i % keyLen]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    for m in range(plainLen):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystreamList.append(k)
        cipherList.append(k ^ PlainBytes[m])

    return keystreamList, cipherList
