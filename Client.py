# ServerVille Client

# Ohai NCSS people
# MasterServer.py, Farmer.py and Client.py
# are all part of the same server farm system.
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((raw_input("IP Address: "), 9002))

if raw_input("Program or data: ")[0].lower() == 'p':
	print "Program"
	path = raw_input("Farmer program path: ")
	f = open(path, 'r')
	f = f.readlines()
	path = raw_input("Server program path: ")
	s = open(path, 'r')
	s = s.readlines()
	name = raw_input("Program name: ")
	client_socket.send("PRGM!" + name)
	client_socket.recv(512)
	client_socket.send("FARM %d" % len(f))
	for line in f:
		client_socket.send(line)
		client_socket.recv(512)
	client_socket.send("SERV %d" % len(s))
	client_socket.recv(512)
	for line in s:
		client_socket.send(line)
		client_socket.recv(512)
	back = client_socket.recv(512)
	print "Done.\nServer Message: " + back + "\nDisconecting...",
	client_socket.close()
	print "Done."
else:
	print "Data"
	path = raw_input("Path: ")
	prgm = raw_input("Program name: ")
	client_socket.send("DATA!" + prgm + "!" + path)
	print "Waiting for reply...",
	back = client_socket.recv(512)
	print "Done.\nServer Message: " + back
	print "Disconecting...",
	client_socket.close()
	print "Done.\n"
	print "Server processing will continue to run in the background."


