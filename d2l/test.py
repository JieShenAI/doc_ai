# Created by JieShen at 2022/3/3 21:41

# %matplotlib inline
# import math
import time
import numpy as np
from utils import d2l


# import torch
# from d2l import torch as d2l

class Timer:
    """记录多次运行时间"""

    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """启动计时器"""
        self.tik = time.time()

    def stop(self):
        """停止计时器并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """返回平均时间"""
        return sum(self.times) / len(self.times)

    def sum(self):
        """返回时间总和"""
        return sum(self.times)

    def cumsum(self):
        """返回累计时间"""
        return np.array(self.times).cumsum().tolist()


if __name__ == '__main__':
    timer = d2l.Timer()
    for X in range(10**7):
        continue
    t = f'{timer.stop():.2f} sec'
    print(t)
