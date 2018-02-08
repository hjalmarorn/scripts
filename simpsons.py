#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
import os,sys
import random
import subprocess
def simpsons():
	if(len(sys.argv) > 1):
		path = sys.argv[1]
	else:
		path = '/Users/hjelmut/Helmut/Þættir/Simpsons'
	cont = False
	while not cont:
		foldersize = len(os.listdir(path)) 
		season = random.randint(1, foldersize)
		seasonPath = os.listdir(path)[season]
		seasonPath = os.path.join(path, seasonPath)
		foldersize = len(os.listdir(seasonPath))
		episode = random.randint(1, foldersize)
		print('Season: ', season, 'Episode: ', episode)
		episode= os.listdir(seasonPath)[episode]
		print(episode)
		finalpath = os.path.join(seasonPath, episode)
		choice = input('Ertu sátt/ur með þennan þátt? (y/n)')
		if choice == 'y':
			cont = True
		else:
			continue

	subprocess.call(['open', finalpath])

simpsons()
