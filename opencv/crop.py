# Created by JieShen at 2022/3/3 16:41

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")


def crop1(img: np.ndarray):
    width, height = 250, 350
    pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))

    cv2.imshow("Image", img)
    cv2.imshow("Output", imgOutput)

    cv2.waitKey(0)


if __name__ == '__main__':
    crop1(img)
