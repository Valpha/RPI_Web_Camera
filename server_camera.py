import socket
import time
from zerocopy import *
import cv2
import io
from PIL import Image
import numpy as np
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("10.9.93.163", 9999))
sock.listen(2)# 监听端口

# 等待数据源端连接
src, src_addr = sock.accept()
print("Source Connected by", src_addr)
f = src.makefile()
# 等待目标端连接
# dst, dst_addr = sock.accept()
# print("Destination Connected by", dst_addr)
cv2.namedWindow("camera")
while True:
    msg = f.read()
    if not msg:
        break
    # print(len(msg), msg[-2])
    # 将'\-n'换回来成'\n'
    # jpeg = msg.replace("\-n", "\n")
    buf = io.BytesIO(msg[0:-1])  # 缓存数据
    buf.seek(0)
    pi = Image.open(buf)  # 使用PIL读取jpeg图像数据
    # img = np.zeros((640, 480, 3), np.uint8)
    img = cv2.cvtColor(np.asarray(pi), cv2.COLOR_RGB2BGR)  # 从PIL的图像转成opencv支持的图像
    buf.close()
    cv2.imshow("camera", img)  # 实时显示
    if cv2.waitKey(10) == 27:
        break

src.close()
sock.close()
