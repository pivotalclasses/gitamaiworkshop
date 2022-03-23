import json

# some JSON:
x='[{"name":"John","age":30,"city":"New York"},'+'{"name":"Kennedy","age":40,"city":"Los Angels"}]'

# parse x:
y = json.loads(x)#forms well-formed JSON

for row in y:
	for col in row:
		print(row[col],"\t", end='')
	print("\n", end='')