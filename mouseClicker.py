import os
import time

os.system("cliclick m:450,300")

start_time = time.time()

for _ in xrange(20*60):
	os.system("cliclick c:.")
	# os.system("cliclick -m verbose -r m:. c:.")

print("--- %s seconds ---" % (time.time() - start_time))

os.system("cliclick -m verbose c:.")