import os

class Utils:
	
	def flatten_list(iterable):
	    	for i in iterable:
	    		if hasattr(i, '__iter__'):
	    			for subi in flatten_list(i):
	    				yield subi
	    		else:
	    			yield i

	a = ['hacked', 'the', ['main', 'frame', 123]]
	print list(flatten_list(a))

