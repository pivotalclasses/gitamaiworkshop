import xml.dom.minidom as MD

tree = MD.parse('items.xml')
# all items data
print('Expertise Data:')
expertise = tree.getElementsByTagName('item')

for elem in expertise:
	print(elem.getAttribute('name') 
		+ "->" + elem.getAttribute('score'))