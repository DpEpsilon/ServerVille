# farmers: list of farmer sockets
# dat: file object of data
# output: output string

length = int(dat.readline())
del dat

for i in xrange(len(farmers)):
	if i != len(farmers) - 1:
		farmers[i].send("%d %d" % (length/len(farmers)*i,length/len(farmers)*(i+1)))
	else:
		farmers[i].send("%d %d" % (length/len(farmers)*i, length))

total = 0
for i in xrange(len(farmers)):
	total += int(farmers[i].recv(512))

output = str(total)
