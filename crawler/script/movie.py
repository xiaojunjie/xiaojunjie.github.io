#-*-coding:utf-8-*-
from urllib.request import urlopen
from urllib.request import urlretrieve
from threading import Timer
from bs4 import BeautifulSoup
import os
import time
import re


root = "../../"
url = {
	"host": "http://www.dy2018.com",
	"last": "/html/gndy/dyzz/",
	"data": root+"_data/movie.yml",
	"temp": "movie_template.txt",
	"log" : root+"log/moive.txt",
	"storage" : "",
	"cloud" :""
}



def git():
	shell = [
		"git -C "+root+" add .",
		"git -C "+root+" commit -m 'send from my crawler' ",
		"git -C "+root+" pull",
		"git -C "+root+" merge",
		"git -C "+root+" push "
	]
	gitResult=""
	for i in shell:
		gitResult += os.popen(i).read()
		time.sleep( 10 )
	outlog(gitResult)



def outlog(txt):
	log  = open(url["log"],"a+")
	log.write(time.strftime("\r\n\r\n----%Y-%m-%d %H:%M:%S-------\r\n", time.localtime()))
	log.write(txt)
	log.close()

def outdata(html):
	# dat  = open(url["data"],"w+")
	# temp = open(url["temp"],"r")
	# yml  = str(temp.read())+"\r\n\r\n"
	bsObj = BeautifulSoup(html,"lxml")
	div = bsObj.find("div",{"class":"co_content222"})
	movie = div.findAll("a")
	print(movie[0])
	# for a in div.findAll("a"):
	# 	run(url['host']+a["href"],getFtp)
		
    # dat.close()
	# temp.close()
def getFtp(html):
	bsObj = BeautifulSoup(html,"lxml")
	a = bsObj.findAll("a")
	for item in a:
		print(item)
		# item["aywrgfek"] and print(item["aywrgfek"])
	# print(xunlei)

def run(url,resolve):
	try:
		html = urlopen(url)
	except Exception as e:
		outlog(url+str(e))
	else:
		resolve(html.read())
	# finally:
	# 	swift()
		# git()

run(url['host'],outdata)
# for i in range(0,6*24):
# 	Timer(600*i, run ).start()
