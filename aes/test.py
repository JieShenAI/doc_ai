# Created by JieShen at 2022/3/1 19:08

if __name__ == '__main__':
    in_file = "in.png"
    out_file = "out.png"
    plain = "plain.png"

    with open(in_file, 'rb') as f_in:
        t = f_in.read(16)
        print(t)

    with open(plain, 'rb') as f_out:
        t = f_out.read(16)
        print(t)
