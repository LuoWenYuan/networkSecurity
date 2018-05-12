# -*- coding:utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import  PKCS1_v1_5
from  Crypto.Hash import  SHA
import base64
# 使用私钥对内容进行签名
def ensignature(user,data):
    with open(user+'-private.txt','rb') as f:
        key = f.read()
        rsaKey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsaKey)
        h = SHA.new()
        sign = signer.sign(h)
        signature = base64.b64encode(sign)
    return signature

# 验证签名
def verifySignture(user,data,signature):
    with open(user + '-public.txt','rb') as f:
        key = f.read()
        rsaKey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsaKey)
        h = SHA.new()
        isVerify = signer.verify(h, base64.b64decode(signature))
    return isVerify

if __name__ == '__main__':
    with open('message.txt', 'rb') as f:
        data = f.read()

    user="Alice"
    signature=ensignature(user,data)
    print(signature)
    isVerify=verifySignture(user,data,signature)
    print(isVerify)