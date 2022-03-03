# cv2

在cv2的矩阵中，0代表黑色

## install

`pip install opencv-python`

### import

`import cv2`

## 图片

### 读取图片

```python
cv2.imread(path)
```

### 展示图片

```python
cv2.imshow("description",img)
```

等待键盘输入后，再退出循环。

```python
cv2.waitKey(0)
```

若希望键盘输入q后，才退出

```python
while True:
	if cv2.waitKey(1) & 0xFF == ord('q'):
    	break
```

## 绘图

在opencv中

![image-20220303153858728](readme.assets/image-20220303153858728.png)





```python
matrix = np.zeros((300, 600, 3), np.uint8)
```



绘制一条直线

![image-20220303154601264](readme.assets/image-20220303154601264.png)

```python
def draw_line(img: np.ndarray):
    start = (0, 0)
    end = (img.shape[1], img.shape[0])
    color = (0, 0, 255)
    thickness = 3
    cv2.line(img, start, end, color, thickness)

draw_line(matrix)
cv2.imshow("line", matrix)
```

`cv2.line()` start起点，end终点，thickness线的宽度；

通过cv2.line实现对图片矩阵数值的修改后，再通过cv2.imshow展示图片。

## 参考资料

basic tutorial
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours

cv pro
https://www.bilibili.com/video/BV18B4y1c7r4

