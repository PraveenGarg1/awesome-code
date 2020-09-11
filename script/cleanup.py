import os
import time
import commands
import sys


if len(sys.argv) < 3:
	print "Incorrect no. of arguments.\n\npython cleanup.py <cleanupPath> <sla in hours>\nE.g. python cleanup.py /data/test_CFI 100\n"
	sys.exit(0)

cleanupPath = sys.argv[1]
cleanupSLA = int(sys.argv[2])*3600

while(1):

	currentTime = int(time.time())

	listOfFiles = commands.getoutput("ls -ltr %s | awk '{print $NF}' | grep GVS" %cleanupPath)

	listOfFiles = listOfFiles.split("\n")

	for file in listOfFiles:
		lastmodified= int(os.stat('%s/%s' %(cleanupPath,file)).st_mtime)

		if (lastmodified < (currentTime - cleanupSLA)):
			#print "%s" %file
			os.system("rm -rf %s/%s" %(cleanupPath,file))
		else:
			print "Cleanup Finished. Sleeping..."
			break
	time.sleep(3600)
