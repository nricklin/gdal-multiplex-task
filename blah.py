
try:
	asdf
except Exception as e:
	print "trying to handle exception"
	raise Exception('shit the exception didint work')

finally:


	print "finally"
	raise Exception('oh shit')