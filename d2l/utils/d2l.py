# Created by JieShen at 2022/3/3 22:11

import torch
import time


def synthetic_data(w, b, num_examples):
    """
    根据真实w,真实b,生成对应的label
    num_examples为生成的数量
      y = Xw + b + noise
    """
    x = torch.randn(num_examples, len(w))
    y = torch.matmul(x, w) + bimport
    # noise
    noise = torch.normal(0, 0.01, y.shape)
    y += noise
    return x, y.reshape(-1, 1)


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
