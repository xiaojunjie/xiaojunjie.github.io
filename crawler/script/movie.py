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

def dy2018(html):
	bsObj = BeautifulSoup(html,"lxml")
	div = bsObj.find("div",{"class":"co_content222"})
	movie = div.findAll("a")
	for x in range(1,len(movie)-1):
		run(url['host']+movie[x]["href"],getFtp)
		# time.sleep( 10 )
		
    # dat.close()
	# temp.close()
def getFtp(html):
	dat  = open(url["data"],"a+")
	temp = open(url["temp"],"r")
	yml  = str(temp.read())+"\r\n\r\n"
	bsObj = BeautifulSoup(html,"lxml")
	title = bsObj.find('title').getText()
	table = bsObj.findAll("div",{"id":"Zoom"})[0].find("table")

	if table:
		for item in table.findAll("a"):
			dat.write(yml % (title,item["href"]))
			print(title)
			print(item.getText())
	dat.close()
	temp.close()

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

run(url['host'],dy2018)
# for i in range(0,6*24):
# 	Timer(600*i, run ).start()
