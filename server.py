import socket

#server settings
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

def main():
    #create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #bind the socket to address and port
    server_socket.bind((SERVER_IP, SERVER_PORT))
    
    #server starts listening and prints to console
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")
    
    try:
        #infinite loop to continuously handle incoming messages
        while True:
            #receive message from client, along with the client's address
            message, client_address = server_socket.recvfrom(BUFFER_SIZE)
            #print received message and client address
            print(f"Received from {client_address}: {message.decode()}")

            #prepare response by appending a humorous message to original message
            response_message = message.decode() + " - Here’s a joke: Why don't skeletons fight each other? They don't have the guts."
            #send the response back to the client
            server_socket.sendto(response_message.encode(), client_address)
    except KeyboardInterrupt:
        #if interrupted by keyboard (Ctrl+C), print shutdown message
        print("Server is shutting down.")
    finally:
        #ensure socket is closed on exit
        server_socket.close()

if __name__ == "__main__":
    main()
