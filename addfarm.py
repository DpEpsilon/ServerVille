#farm_socket (Socket to the server)

nums = farm_socket.recv(512).split()
lower = int(nums[0])
higher = int(nums[1])
a = 0
for i in xrange(lower, higher):
	a += i
farm_socket.send(str(a))
