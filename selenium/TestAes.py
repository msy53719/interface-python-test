# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 16
BS = AES.block_size
PADDING = '\0'
pad_it = lambda s: s+(BS - len(s)%BS)*PADDING
key = 'krstuvwsyz01sodm'
#iv = '16bit'

sourceStr='http://api.eqter.com'
generator = AES.new(key,AES.MODE_CBC,'0000000000000000')
crypt = generator.encrypt(pad_it(key+sourceStr))
cryptedStr = base64.b64encode(crypt)


print cryptedStr