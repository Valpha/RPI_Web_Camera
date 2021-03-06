import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("10.5.3.187", 12000))# 注意bind的这里，IP地址和端口号都要与前面的程序中一样
sock.listen(2)# 监听端口

# 等待数据源端连接
src, src_addr = sock.accept()
print "Source Connected by", src_addr

# 等待目标端连接
dst, dst_addr = sock.accept()
print "Destination Connected by", dst_addr

while True:
    msg = src.recv(1024 *1024)
    if not msg:
        break
    try:
        dst.sendall(msg)
    except Exception as ex:
        dst, dst_addr = sock.accept()
        print "Destination Connected Again by", dst_addr
    except KeyboardInterrupt:
        print "Interrupted"
        break

src.close()
dst.close()
sock.close()
