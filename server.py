import socket
import random

SERVER_ADDRESS = ('localhost', 8686)

def check_number(number: int,  arg: int):
	if arg > number:
		return 'more'
	elif arg < number:
		return 'less'
	elif arg == number:
		return 'correct'

if __name__  == "__main__":
	sock = socket.socket()
	sock.bind(SERVER_ADDRESS)
	sock.listen(1)
	conn, addr = sock.accept()

	print("connected:"+str(addr))
	number = random.randint(1,10)
	while True:
		data = conn.recv(1024)
		if not data:
			conn.close()
			break
		command, arg = data.decode('utf-8').split(' ')
		if command == 'guess':
			result = check_number(number,int(arg))
			conn.send(result.encode('utf-8'))
