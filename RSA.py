# -*- coding:utf-8 -*-
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

def rsaEncript(data,nameSender,nameReceiver):
    # print(data)
    # # 用Sender的私钥加密
    # with open(nameSender+'-private.txt', 'rb') as f:
    #     key = f.read()
    #     rsakey = RSA.importKey(key)  # 导入读取到的私钥
    #     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    #     data = base64.b64encode(
    #         cipher.encrypt(data))
    # print(data)

    # 用Receiver的公钥加密
    with open(nameReceiver+'-public.txt', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的私钥
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
        data = base64.b64encode(
            cipher.encrypt(data))

    return data

def rsaDecript(data, nameSender, nameReceiver):
    # 用Receiver的私钥解密
    with open(nameReceiver + '-private.txt', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的私钥
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
        data = cipher.decrypt(base64.b64decode(data), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str

    # # 用Sender的公钥解密
    # with open(nameReceiver + '-private.txt', 'rb') as f:
    #     key = f.read()
    #     rsakey = RSA.importKey(key)  # 导入读取到的私钥
    #     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    #     data = cipher.decrypt(base64.b64decode(data), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    return data

# 生成name的公私秘钥并且存储在文件里
def generateKey(name):
    # 伪随机数生成器
    random_generator = Random.new().read
    # print(random_generator)

    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)

    # 秘钥对的生成与存储
    private_key = rsa.exportKey()
    with open(name+'-private.txt', 'wb') as f:
        f.write(private_key)

    public_key = rsa.publickey().exportKey()
    with open(name+'-public.txt', 'wb') as f:
        f.write(public_key)

if __name__ == '__main__':

    #读取信息
    with open('message.txt', 'rb') as f:
        data = f.read()
    #生成Alice和Bob的秘钥对
    personOne="Alice"
    personTwo="Bob"
    generateKey(personOne)
    generateKey(personTwo)

    #以Alice发送给Bob的形式来加密
    data=rsaEncript(data,personOne,personTwo)
    print(data)
    # 写入加密文件
    with open('ciphertextRSA.txt', 'wb') as f:
        f.write(data)
    # 解密，从加密文件中读取密文
    with open('ciphertextRSA.txt', 'rb') as f:
        data = f.read()
        data=rsaDecript(data,personOne,personTwo)
        print(data)


