import socket
import sys

sock = socket.socket ()

try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
except socket.error as err:
    print("Failed to create a socket")
    print("Reason :"+str(err))
    sys.exit()
print("Socket Created")
target_host = input("Enter target host address : ")
target_port = input("Enter target port number : ")

try:
    sock.connect((target_host,int(target_port)))
    print("Connected to : "+target_host+target_port)
    sock.shutdown(2)
    
except socket.error as err:
    print("Failed to connect : "+target_host+target_port)
    print("Reason : "+str(err))
    sys.exit()



    