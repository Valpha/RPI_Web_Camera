from socket import *
import numpy
from zerocopy import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('',25000))
s.listen(1)
c,a = s.accept()
a = numpy.arange(0.0,500.0)
send_from(a,c)
