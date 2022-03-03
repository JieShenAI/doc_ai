# Created by JieShen at 2022/3/1 18:28

"""
由于字节的长度需要为16的整数bei
"""

if __name__ == '__main__':
    text = "整sd"
    text_byte = text.encode()
    # while len(text_byte) % 16 != 0:
    #     text_byte += b'0'
    # print(text_byte)
    print(len(text_byte))
    # a = 10
    # print(a.to_bytes())

    text_byte += ('0' * 11).encode('utf-8')
    print(len(text_byte))
