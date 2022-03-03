# Created by JieShen at 2022/3/1 20:36

"""
对于一个文件如何拿到最后一个字节的内容
"""
a = "法法".encode()
print(a)
a += b'0'
print(a)
print(a.decode())
# 所以额外要多16bit存放信息
n = 5

fill_byte = n.to_bytes(1, "little")
fill_byte += "JieJie".encode()
print(fill_byte)
print(len("".encode()))

import time

t = time.localtime()
time_f = lambda x: str(x).zfill(2)
time_f(t.tm_year) + time_f(t.tm_mon) + time_f(t.tm_mday)
# print(now)


print('*' * 20)
from jshen.j_time import get_year_mon_day

t = get_year_mon_day()
print(t)

import os

img_size = os.path.getsize("../aes/in.jpg")
img2_size = os.path.getsize("../aes/decencin.jpg")
print(img_size)
print(img2_size)
with open("../aes/decencin.jpg", 'rb') as f:
    data = f.read(img2_size - 6)
    f.close()
    with open("new.jpg", 'wb') as f2:
        f2.write(data)
        f2.close()

