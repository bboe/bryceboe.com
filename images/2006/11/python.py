#!/usr/bin/python
import sys,threading,md5,Queue

# This is the threaded class
class Process(threading.Thread):
	def __init__(self,ids,results):
		threading.Thread.__init__(self)
		self.ids = ids
		self.results = results
	def run(self):
		while True:
			# Once ids is empty stop the thread
			if self.ids.empty():
				break
			# The queue can become empty inbetween
			# the previous check and now, so set
			# 1 second timeout and handle the error
			# returned.
			# The except block could break there, but since
			# it is handled above we will just continue.
			try:
				t = self.ids.get(True,1)
			except Queue.Empty:
				continue
			p = breakHash(t)
			self.results.put(p)

# This brute forces the original string from the hash.
def breakHash(hash):
	for x in range(3000):
		if md5.new(str(x)).hexdigest() == hash:
			return hash,x
	return hash,1
			
def main():
 	# Create blocking queue from input
	ids = Queue.Queue(0)
	for line in sys.stdin:
		ids.put(line[:-1])
	# Create blocking queue for output		
	results = Queue.Queue(ids.qsize())

	# Create and start all threads
	myThreads = []
	for x in range(3):
		c = Process(ids,results)
		myThreads.append(c)
		c.start()
	
	# The main() thread will stay here until
	# all other threads are complete
	for thread in myThreads:
		thread.join()
	
	# Get the results and send them to the next function
	for x in range(results.qsize()):
		t = results.get()
		# Handle error if pipe is closed
		try:
			print t[0],"\t",t[1]
		except IOError:
			sys.exit(1)
	
if __name__ == '__main__':
	main()