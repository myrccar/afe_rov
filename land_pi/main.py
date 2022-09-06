#script for land pi 
#tested on my pc only
from pstats import SortKey
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(socket.gethostname(),6060)
s.listen(5)