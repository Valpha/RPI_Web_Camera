from socket import *
import numpy
from zerocopy import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost',25000))
a = numpy.zeros(shape=500, dtype=float)
print(a[0:10])
recv_into(a,c)
print(a[0:10])

