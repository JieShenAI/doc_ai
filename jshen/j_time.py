# Created by JieShen at 2022/3/1 21:08

import time


def get_year_mon_day():
    t = time.localtime()
    time_f = lambda x: str(x).zfill(2)
    return time_f(t.tm_year) + time_f(t.tm_mon) + time_f(t.tm_mday)
