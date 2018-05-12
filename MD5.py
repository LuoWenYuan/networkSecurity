# -*- coding:utf-8 -*-
from Crypto.Hash import MD5

def generateMD5(data):

    hash = MD5.new()
    hash.update(data)#注意，必须转化为二进制的形式
    # print(hash.digest())
    return hash.digest()

if __name__ == '__main__':
    # 生成MD5值
    with open('message.txt', 'rb') as f:
        data = f.read()
    data = generateMD5(data)
    # 将MD5值存储在文件中
    with open("MD5OfMessage.txt",'wb') as  f:
        f.write(data)

    # 读取MD5文件并输出
    with open("MD5OfMessage.txt", 'rb') as  f:
        data=f.read();
        print(data)
1