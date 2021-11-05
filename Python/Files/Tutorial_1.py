#open

#filehandle
a = open("abc.txt","a")

#WORK
		# TEXT
	# read : read()
'''
data = a.read()
print(data)
'''

	# write : write()
"""
a.write("new data")
"""

	# append : write()
a.write(" new data 2")


#close
a.close()
