# Created by JieShen at 2022/3/2 16:04

import cv2
import numpy
import numpy as np

img_path = "Resources/lena.png"
kernel = np.ones((5, 5), np.uint8)


def get_img(path: str):
    img = cv2.imread(path)
    return img


def img_read(img):
    img = cv2.imread(img)
    cv2.imshow("output", img)
    cv2.waitKey(0)


def video_read():
    cap = cv2.VideoCapture("Resources/record_test.mp4")
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def camera():
    cap = cv2.VideoCapture(0)  # 若有多个摄像头，在这更改摄像头的编号
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 100)  # 调整亮度
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        # cv2.imshow("Video", img2gray(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def img_path_gray(img_path: str):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray img", img_gray)
    cv2.waitKey(0)


def img2gray(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


def img_show(mat: str, img: numpy.ndarray, t=0):
    cv2.imshow(mat, img)
    cv2.waitKey(t)


def img_blur(img: numpy.ndarray):
    return cv2.GaussianBlur(img, (7, 7), 0)  # kernel size必须是奇数


def edge_detect(img: numpy.ndarray):
    """
    canny
    :return:
    """
    return cv2.Canny(img, 100, 100)


def img_dilate(img):
    """
        canny
        :return:
        """

    img_canny = edge_detect(img)
    return cv2.dilate(img_canny, kernel, iterations=1)  # iterations 厚度


def img_erode(img):
    """
    eg:
    img = get_img(img_path)
    cv2.imshow("raw", img)
    cv2.imshow("edge", edge_detect(img))
    d = img_dilate(img)
    cv2.imshow("dilate", d)
    cv2.imshow("erode", img_erode(d))
    cv2.waitKey(0)

    :param img:
    :return:
    """
    return cv2.erode(img, kernel, iterations=1)


def img_resize(img: np.ndarray):
    """
    img = get_img(img_path)
    cv2.imshow("raw", img)
    resize = img_resize(img)
    cv2.imshow("resize", resize)
    :param img:
    :return:
    """
    return cv2.resize(img, (500, 300))


def crop(img, x1, x2, y1, y2):
    """
    :param img:
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :return:
    """
    return img[x1:x2, y1:y2]


if __name__ == '__main__':
    img = get_img(img_path)


    cv2.imshow("raw",img)
    img_crop = crop(img, 200, 300, 200, 300)
    cv2.imshow("crop",img_crop)

    cv2.waitKey(0)
