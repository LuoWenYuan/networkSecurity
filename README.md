存储密文和签名时都采用了base64编码，避免乱码
1.Vigenere算法
思路比较简单清晰，自定义了一个key作为秘钥
2.DES算法
使用了pyDES第三方库，自定义了秘钥key和偏转向量iv，因为要求为64位，就是8个字节，因为Python默认的是utf-8编码，所以只要输入要求key和iv的字符串长度为8
注意:写入byte类型文件时，当转换为str类型时，前缀b的位置会报错，所以采用open('ciphertextDES.txt', 'wb')的形式，以二进制的方式写入文件，读取解密时也直接以二进制的形式读取
3.RSA 算法
由于pyDES库只含有DES算法，所以此处换了个第三方库Crypto
注意：在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
4.用Crypto库实现了生成md5值得操作
5.数字签名验证：
采用RSA数字签名验证方式，直接使用前面RSA生成的密文和明文

注:
    （1）所有文件都用txt格式保存。
    （2）参考文献：
                《计算机安全与保密 》作者：李辉
                cycrypo文档https://www.dlitz.net/software/pycrypto/api/current/
                python官方网站https://www.python.org

    （3）本代码在MacOS下基于python3.6的环境测试实现
