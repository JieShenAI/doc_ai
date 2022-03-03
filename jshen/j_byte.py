# Created by JieShen at 2022/3/1 21:49

from j_time import get_year_mon_day


def fill_byte(b, *args):
    for p in args:
        if type(p) == int:
            for i in range(p):
                b += b'0'
            b += p.to_bytes(8, "little")
        elif type(p) == str:
            b += p.encode()
    return b


if __name__ == '__main__':
    b = "北京欢迎你".encode()

    # print(len(b))
    # print(b)
    # t = get_year_mon_day()
    # new_byte = fill_byte(b, 1, t)
    # print(new_byte, len(new_byte))
    # n = 219
    # num = n.to_bytes(1, "little")
    # print(num, len(num))
    b = b'0'
    print(b, len(b))

    c = 'c'.encode()
    print(c, len(c))
