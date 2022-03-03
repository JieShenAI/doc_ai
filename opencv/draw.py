# Created by JieShen at 2022/3/2 20:54

import numpy as np
import cv2

matrix = np.zeros((300, 600, 3), np.uint8)


def fill_same(b=0, g=0, r=0):
    """
    给三个通道赋值
    eg:
    b,g,r = 255,255,255 is white
    :param b:
    :param g:
    :param r:
    :return:
    """
    # set color
    matrix[:] = b, g, r
    cv2.imshow("img", matrix)


def draw_line(img: np.ndarray):
    start = (0, 0)
    end = (img.shape[1], img.shape[0])
    color = (0, 0, 255)
    thickness = 3
    cv2.line(img, start, end, color, thickness)


def draw_rectangle(img: np.ndarray):
    start = (200, 100)
    end = (img.shape[1], img.shape[0])
    color = (0, 255, 0)
    cv2.rectangle(img, start, end, color, cv2.FILLED)


def draw_circle(img: np.ndarray):
    center = (300, 150)
    radius = 150
    color = (0, 0, 255)
    thickness = 3
    cv2.circle(img, center, radius, color, thickness)


def text(img: np.ndarray):
    cv2.putText(img, "Great Again", (300, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)


if __name__ == '__main__':
    while True:
        text(matrix)
        cv2.imshow("circle", matrix)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # fill_same(r=255)
    # print(matrix.shape)
    # cv2.waitKey('q')
