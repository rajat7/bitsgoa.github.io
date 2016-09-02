import pandas as pd
import os
from shutil import copytree, copyfile
import urllib
from bs4 import BeautifulSoup
import random

data = pd.read_csv('test.csv')

for row in data.itertuples():
	name = row[2].replace(" ", "").lower()
	try:
		newpath = r'/Users/mridul/dev/bitsgoa.github.io/{}'.format(name)
	#	if not os.path.exists(newpath):
	#		os.makedirs(newpath)
	#	else:
	#		print 'already present' 
	#	os.chdir(newpath)
		if not os.path.exists(newpath):
			copytree('/Users/mridul/dev/bitsgoa.github.io/user7', '/Users/mridul/dev/bitsgoa.github.io/{}/'.format(name))
		else:
			rand = random.randint(1, 1000)
			copytree('/Users/mridul/dev/bitsgoa.github.io/user7', '/Users/mridul/dev/bitsgoa.github.io/{}{}/'.format(name, rand))
		os.chdir(newpath)
		copyfile('/Users/mridul/Desktop/students/{}.jpg'.format(row[1]), '/Users/mridul/dev/bitsgoa.github.io/{}/assets/img/avatar.jpg'.format(name))	
		page = urllib.urlopen('/Users/mridul/dev/bitsgoa.github.io/{}/index.html'.format(name)).read()
		soup = BeautifulSoup(page)

		for node in soup.find_all("h3", {"id": "name_field"}):
			print node
			node.replace_with(row[2])

		html = soup.prettify()
		with open("index.html", "wb") as file:
			file.write(html)
	# print dir(page)
	except:
		print row[1]
