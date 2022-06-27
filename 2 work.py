import socket 
import struct

def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack('!L', int32))
print(int32_to_ip(2154959208))
print(int32_to_ip(0))
print(int32_to_ip(2149583361))