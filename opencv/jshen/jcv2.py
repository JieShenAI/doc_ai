# Created by JieShen at 2022/3/3 18:00

import cv2


def wait_q():
    while True:
        if cv2.waitKey(0) & 0xFF == 'q':
            break
