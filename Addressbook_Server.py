#Reda Rahmoune
import socket
from threading import Thread

# setting up socket
serverport = 8815
servername = socket.gethostname()
# creat a tcp welcoming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((servername, serverport))
# server become listning
s.listen(5)
print("the server is on")


# handle connection of client
def handleConnection(s):
    # receive reply
    answer = s.recv(4096)
    print("> New Request received from : "+answer)
    txt_file = open("database.txt",'r')
      
    for information  in txt_file:
        if answer in information:
            txt_ans = information
        else:
            text_ans="the information doesn't exist in our database "

    s.send(txt_ans)
# keep threads running
while True:

    cs, addr = s.accept()
    # we iniatialize the threat and run it by telling him to execute the handleConnection function and giv
    # and the argument given to the thread were the connection with the client and the value we incriment
    t = Thread(target=handleConnection, args=(cs,))
    # we start the thhread
    t.start()
