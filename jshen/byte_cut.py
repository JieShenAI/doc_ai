# Created by JieShen at 2022/3/1 21:33

"""
字节切割
"""
import os

file_size = os.path.getsize("t.txt")
print(file_size)
with open("t.txt", 'rb+') as f:
    # 拿到最后16个比特
    data = f.read()
    print(data.decode())
    f.close()

print(data, len(data))
print(data[-16::])
