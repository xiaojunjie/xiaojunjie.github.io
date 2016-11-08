#-*-coding:utf-8-*-
#!/usr/bin/env python
from threading import Timer
import movie
import rs

for i in range(0,6):
	Timer(4*3600*i, movie.run ).start()

for i in range(1,6*24):
	Timer(600*i, rs.run ).start()
