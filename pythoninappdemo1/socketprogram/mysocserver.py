#import the socket module
import socket

def server_program():
    host = socket.gethostname() #getting the ip of host
    port = 5000
    #"127.0.01" or "localhost"
    #port can range from 1024 till 65535

    #create socket instance
    server_socket = socket.socket()

    #binding the host ip and port to our socket instance
    #pass the host and port as a tuple into bind method
    server_socket.bind((host,port))

    #start listening to the socket
    server_socket.listen(2)  #2 inside listen represents number of clients

    #accept an incoming connection
    #the accept() method will give back the conn obj and ip address of the incoming connection request
    conn, address = server_socket.accept()
    print("Connection accepted from"+str(address))

    #now we can receive the messages using a while loop
    #keep the connection active and receive messages until there is none
    while(True):
        #infinite while loop to receive the data stream
        #receive the packets (with max size og 1024 bytes)
        #decode the received data
        data = conn.recv(1024).decode()

        # if no data recieved then terminate the while loop
        if not data:
            break

        #if valid data we can print the data recieved
        print("Message from client "+str(address)+" : "+str(data))

        #give provision to send reply back to the client
        data = input('Type reply here : ')
        #encode the data and send it to the client
        conn.send(data.encode())
    
    conn.close() #close the connection once the while loop breaks


#if our python program is imported, then just be there as an imported code and do not run until the user calls the function(default behavior)
#if we directly run it using the command [prog.py]
#then start the function server_program() automatically
if __name__ == '__main__':
    server_program()