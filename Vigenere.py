# -*- coding:utf-8 -*-
import base64
def encrypt(data,key):

    for i in range(len(data)):
        data[i]=(data[i]+key[i%len(key)])%256
    # print(data)
    for i in range(len(data)):
        data[i]=chr(data[i])
    # return data

def decrypt(data,key):
    for i in range(len(data)):
        data[i]=(data[i]-key[i%len(key)])%256
    # print(data)
    for i in range(len(data)):
        data[i]=chr(data[i])
    str=""
    for i in data:
        str+=i
    return str

if __name__ == '__main__':

    with open('message.txt', 'r') as f:
        data = f.read()
        new_data=[]
        # 将字符串转为对应数字数组
        for i in range(len(data)):
            new_data.append(ord(data[i]))
    # 转换为对应数字数组
    key="fenweaiof"
    new_key=[]
    for i in range(len(key)):
        new_key.append(ord(key[i]))
    # 加密
    encrypt(new_data,new_key)

    # print(new_data)
    #存储到密文文件中
    with open("ciphertextVigenere.txt","wb") as f:
        str=""
        for i in range(len(new_data)):
            str+=new_data[i]
        # python3中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码
        str = base64.b64encode(str.encode('utf-8'))
        print(str)
        f.write(str)


    #解密
    for i in range(len(new_data)):
        new_data[i]=ord(new_data[i])

    new_data=decrypt(new_data,new_key)

    print(new_data)