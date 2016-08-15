#!/bin/python
#
#librat.py implements all algorithms used in rat.py including encryption.
#

def check_file_size(arg, dirname, files):
	for file in files:
		filename = os.path.join(dirname,file)
		if os.path.isfile(filename):
			size = os.path.getsize(filename)
			if size > 10000000:
				if arg is None:
					print '%.2fMB %s'%(size/10000000.0,filename)
				elif isinstance(arg,list):
					arg.append((size/10000000.0,filename))

def search_for_files():
	"""
	search for files in the current dirctory.
	"""
	pass

def collect_files():
	"""
	parse and save all files returned by search_for_files.
	"""
	fileList = search_for_files()
	pass
