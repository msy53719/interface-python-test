#coding=utf-8
from Crypto.Cipher import AES
import base64
def aes_encrypt(key,data):
   # key = 'krstuvwsyz01sodm'  # 加密时使用的key，只能是长度16,24和32的字符串
    BS = AES.block_size #16
    iv='16bit'
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(AES.MODE_CBC,key,iv)

    encrypted = cipher.encrypt(pad(key+data))# aes加密
   # encrypted = cipher.encrypt(pad)
    result = base64.b64encode(encrypted)  # base64 encode
    return  result

print aes_encrypt('krstuvwsyz01sodm','http://api.eqter.com')