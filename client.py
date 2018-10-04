import socket

SERVER_ADDRESS = ('localhost', 8686)

if __name__ == "__main__":
	sock = socket.socket()
	sock.connect(SERVER_ADDRESS)
	print("Lets the game begin")
	while True:
		arg = input('Enter the command:')
		send_data = arg.encode('utf-8')
		sock.send(send_data)
	
		data = sock.recv(1024).decode('utf-8')
		print(data)
	
		if data == "correct":
			sock.close()
			break
