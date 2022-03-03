# Created by JieShen at 2022/3/1 20:28
from Crypto.Cipher import AES

# filename = input("请输入要加密的文件名：")

filename = "in.jpg"
# key = input("请输入密码：")
key = "12345678" * 2
# 秘钥,此处需要将字符串转为字节
# key = key + get_bios_id() + get_cpu_id() + get_board_id() + get_disk_id() + get_mac_address()
key = str.encode(key)
if len(key) > 32:  # 秘钥不能超过32
    key = key[0:32]


# 加密内容需要可以被16整除，所以进行空格拼接
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


# 加密秘钥需要可以被16整除，所以进行空格拼接
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


# 进行加密算法，模式ECB模式，把叠加完的秘钥传进来
aes = AES.new(pad_key(key), AES.MODE_ECB)
# 加密内容,此处需要将字符串转为字节

# data = bytearray(os.path.getsize(filename))
with open(filename, 'rb') as f:
    # f.readinto(data)
    data = f.read()
    f.close()

# 将数据传入加密类中，结果为字节类型
encrypted_data = aes.encrypt(pad(data))

with open("enc" + filename, 'wb') as f:
    f.write(encrypted_data)
f.close()


print("成功，请查看文件夹下" + "enc" + filename)
