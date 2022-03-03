# 环境

## tensorflow

擅长静态图

## PyTorch

擅长动态图

# intro

video: https://www.bilibili.com/video/BV1mZ4y1P7y4

介绍：做一个智能驾驶的模型。
论文下载：p=21；14:30

# 数据处理

## 图片正则化

图片的范围是[0,250]，希望数据样本的均值是0，方差为1。

处理是：`X = X /250 - 0.5`

> 即使不处理，网络也是可以学到的，但是这样可以减轻网络的负担。

## Batch Normlization

对batch进行正则化



