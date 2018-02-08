#!/usr/local/bin/python3
import threading, os, sys

def pause():
	os.system("killall Safari")


try:
        if(len(sys.argv) == 1):
	        time = 2.0;
        else:
	        time = float(sys.argv[1]) * 60
        t = threading.Timer(time, pause)
        t.start()
except():
        sys.exit()
