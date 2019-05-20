from socketserver import BaseRequestHandler, UDPServer
import cv2
from picamera import PiCamera
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connecting from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)
def camera_capture(resolution):
    camera = PiCamera()
    camera.resolution = (resolution)
    camera.start_preview()
    sleep(2)
    caaamer.capture(stream,'jpeg')


if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()

