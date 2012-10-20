# ServerVille Farmer

# Ohai NCSS people
# MasterServer.py, Farmer.py and Client.py
# are all part of the same server farm system.
import socket
farm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
farm_socket.connect((raw_input("IP Address: "), 9001))

while (1):
	print "Awaiting further instructions...",
	print "Receiving...",
	head = farm_socket.recv(512).split()
	farm_socket.send("k")
	program = ""
	for i in xrange(int(head[1])):
		program += farm_socket.recv(1024)
		farm_socket.send("k")
	print "Done."
	print "Waiting for server to start procedure..."
	farm_socket.recv(512)
	print "Executing...",
	exec(program)
	print "Done."
