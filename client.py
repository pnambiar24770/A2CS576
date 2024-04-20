import socket

#server settings
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def main():
    #create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #define the message to be sent
    message = "Hello"
    #send the message to server
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    #print to console what message was sent
    print(f"Your client program sends “{message}”")
    
    #wait for and receive the response from the server
    response, _ = client_socket.recvfrom(1024)
    #print received response
    print("Your client program would receive the string:", response.decode())
    
    #close the socket after communication is complete
    client_socket.close()

if __name__ == "__main__":
    main()
