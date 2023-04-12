import cv2
import numpy as np

# 读入多张图片
image1 = cv2.imread("test/2.jpg")
image2 = cv2.imread("test/3.jpg")

# 拼接图片
result = np.hstack([image1, image2])

# 保存拼接后的图片
cv2.imwrite("test/long_image.jpg", result)