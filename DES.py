# -*- coding:utf-8 -*-
import sys
import importlib
import base64
importlib.reload(sys)
from pyDes import *
#加密函数，调用了pyDes库的encrypt函数，返回加密后的密文
def desEncript(data,key,iv):

    # 使用DES对称加密算法的CBC模式加密
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    return d
#解密函数，调用了pyDes库的decrypt函数，返回解密后的明文
def desDecript(data,key,iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    d = k.decrypt(data)
    return d

if __name__ == '__main__':

    with open('message.txt', 'r') as f:
        data = f.read()
    key = "12345678"    #密钥
    iv = "87654321" # 偏转向量

    #加密
    data=desEncript(data,key,iv)
    print(data)
    # for i in data:
    #     print(i)
    #写入加密文件
    with open('ciphertextDES.txt', 'wb') as f:
        f.write(base64.b64encode(data))
    #解密，从加密文件中读取密文
    with open('ciphertextDES.txt', 'rb') as f:

        data=f.read()
        data=base64.b64decode(data)
    data=desDecript(data,key,iv)
    data=data.decode("utf-8")
    print(data)
    # print(d)
    # print ("Decrypted: %r" % k.decrypt(d))