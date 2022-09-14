#import the socket module
import socket

def client_program():
    host = socket.gethostname() #getting the ip of host
    #since both server and client are in the same machine
    #we can get the loopback address as the server address
    port = 5000 #port no in which the server is listening
    
    #create socket instance
    client_socket = socket.socket()

    #instead of binding, in client we are connecting to the server
    client_socket.connect((host,port)) #host and port as tuple

    #getting the message to send to the server
    message = input("Enter the msg to send to the server: ")

    while message.lower().strip() != 'exit':
        #if the message is not 'exit' send it to the server
        client_socket.send(message.encode())

        #receive any reply data from the server
        data = client_socket.recv(1024).decode()
        
        #printing the received text
        print("Received from server: "+data)

        #getting the message to send to the server
        message = input("Enter the msg to send to the server: ")

    #close the socket once the while loop is exited
    client_socket.close()

if __name__ == '__main__':
    client_program()