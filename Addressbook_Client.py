
#Reda rahmoune
import socket


# creat a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creat the authentifaction to connect with the serverv
hostname = socket.gethostname()
# ip_client = socket.gethostbyname(hostname)
tcp_port = 8815

# create TCP connection socket for server and port
client_socket.connect((hostname, tcp_port))

# print when the server answer the client requet to connect
# message = client_socket.recv(4096).decode()
# print("message recu du server : ")

# send an input who entred by the client to the server
request_string = input("Enter your email: ")
client_socket.send(request_string.encode())

# print the received answer from the server
some_text = client_socket.recv(4096).decode()
print(some_text)


# close the connection
client_socket.close()
