from socket import *
import numpy
from zerocopy import *
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

if __name__ == '__main__':
    stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    # image = Image.open(stream)

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('',25000))
    s.listen(1)
    '''内存地址传输，a为address的首地址，直接传输内存使用send_from'''
    c,a = s.accept()
    s.send()
    a = numpy.arange(0.0,500.0)
    send_from(a,c)