import socket
HOST = '127.0.0.2' # Standard loopback interface address (localhost)
PORT = 65421 # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            recv_data=conn.recv(1024)
            if(recv_data=="q" or recv_data=="Q"):
                s.close()
                exit(0)
            else:
                print("\n1.SEND ACK\n2.TIME OUT\n")
                opt=input("Enter Option:\n")
                if(opt=="1"):
                    send_data="ack"
                    print("\n RECEIVED DATA=",recv_data )
                else:
                    send_data="timeout"
                conn.sendall(send_data.encode())