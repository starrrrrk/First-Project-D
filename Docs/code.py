#!/usr/bin/env python3
with open('Docs/file.txt') as f:

	variable = f.read().splitlines()
	  
	  #print((len(variable)))
	 
	if len(variable) > 4:
		print(variable.pop(4))
		print("found items bigger than 3. deleting..")
	
	elif len(variable) <= 3:
		print('fine')
	
	with open('Docs/file.txt', 'w') as g:
		for k in variable:
			g.write(k + '\n')
