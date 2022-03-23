 #1. Get the file handler
file = open("data1.txt", "r")#Read Mode
for row in file: #2. Read Each row from array
	cols = row.split(",")#3. Split row based on delimiter
	for col in cols:#4. Read each column
		print(col+"\t", end='')
	print("", end='')
file.close()