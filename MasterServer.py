# ServerVille Master Server

# Ohai NCSS people
# MasterServer.py, Farmer.py and Client.py
# are all part of the same server farm system.
import socket
serverf_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverf_socket.bind(("", 9001))
serverf_socket.listen(200)

farmers = []

print "MasterServer Waiting for farmers on port 9001"

while 1:
	farmer_socket, address = serverf_socket.accept()
	print "I got a connection from ", address
	farmers.append(farmer_socket)
	if raw_input("Should I wait for more connections? ").lower()[0] == 'n':
		break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 9002))
server_socket.listen(5)

while 1:
	print "MasterServer Waiting for client on port 9002"
	recv_socket, address = server_socket.accept()
	print "I got a connection from ", address
	print "Waiting for instruction...",
	head = recv_socket.recv(512)
	head = head.split('!')
	recv_socket.send("I am ok, so far.")
	if head[0] == "PRGM":
		print "Receiving program...",
		name = head[1]
		farm = recv_socket.recv(512).split()
		print "Farm Head %s," % repr(farm[0]),
		f = open(name + "_farm.py", "w")
		for i in xrange(int(farm[1])):
			f.write(recv_socket.recv(1024))
			recv_socket.send("k")
		print "Farm Py,",
		del f
		serv = recv_socket.recv(512).split()
		print "Server Head,",
		recv_socket.send("k")
		f = open(name + "_serv.py", "w")
		for i in xrange(int(serv[1])):
			f.write(recv_socket.recv(1024))
			recv_socket.send("k")
		print "Server Py,",
		del f
		recv_socket.send("I am ok. :)")
		print "Done."
	else: # head[0] == "DATA"
		prgm = head[1]
		path = head[2]
		servprg = open(prgm + "_serv.py", "r").read()
		farmprg = open(prgm + "_farm.py", "r").read()
		dat = open(path, "r")
		print "Distributing program to farmers...",
		for f in farmers:
			f.send("PRGM %d" % len(farmprg))
			f.recv(512)
			for line in farmprg:
				f.send(line)
				f.recv(512)
		print "Done."
		output = ""
		print "Executing...",
		for f in farmers:
			f.send("GO")
		exec(servprg)
		print "Done."
		f = open(path + ".out", "w")
		f.write(output)
		del f
