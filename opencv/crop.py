# Created by JieShen at 2022/3/3 16:41

import cv2
import numpy as np
from jshen import jcv2

img = cv2.imread("Resources/lena.png")


def crop1(img: np.ndarray):
    width, height = 250, 350
    pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))

    cv2.imshow("Image", img)
    cv2.imshow("Output", imgOutput)


def hv_stack(img: np.ndarray):
    img_hor = np.hstack((img, img, img))
    img_ver = np.vstack((img_hor, img_hor))
    # cv2.imshow("hor", img_hor)
    cv2.imshow("ver", img_ver)


if __name__ == '__main__':
    hv_stack(img)
    jcv2.wait_q()
