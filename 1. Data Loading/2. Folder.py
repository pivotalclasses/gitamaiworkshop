import os
flist = os.listdir('./testfiles')#Return list of file names in given folder
for item in flist:#Get each file name
	if os.path.isfile('./testfiles/' + str(item)):#Take only files
		fl = open('./testfiles/' + str(item), "r") #Open each file
		for line in fl: #Read from that file
			#Split will divide line into array of cols
			colarray = line.split("#")
			print("\n", end='')
			for col in colarray: #Read each column
				print("\t"+str(col), end='')

		fl.close()