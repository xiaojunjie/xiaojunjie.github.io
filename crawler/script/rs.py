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
	"host": "http://rs.xidian.edu.cn/",
	"forum": "forum.php?mod=forumdisplay&fid=106",
	"data": root+"_data/rs.yml",
	"temp": "img_template.txt",
	"log" : root+"log/ruisi.log",
	"storage" : root+"storage/ruisi/",
	"cloud" :"//static.xjjfly.com/ruisi/",
	"swiftKey": root+"swiftKey"
}



def swift():
	shell = open(url["swiftKey"],"r").readlines()
	shell.append("swift upload storage "+url['storage']+" --object-name ruisi -c")
	shell = " && ".join(shell)
	swiftResult = os.popen(shell).read()
	# for i in shell:
	# 	swiftResult += os.popen(i).read()
	outlog(swiftResult)

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

def imgFetch(host,src):
	localFile  = url["storage"]+src
	originFile = host+src
	localPath  = os.path.dirname( localFile )
	os.path.exists( localPath ) or os.makedirs( localPath )
	os.path.isfile( localFile ) or urlretrieve( originFile, localFile )
	return True

def outlog(txt):
	log  = open(url["log"],"a+")
	log.write(time.strftime("\r\n\r\n----%Y-%m-%d %H:%M:%S-------\r\n", time.localtime()))
	log.write(txt)
	log.close()

def outdata(html):
	dat  = open(url["data"],"w+")
	temp = open(url["temp"],"r")
	yml  = str(temp.read())+"\r\n\r\n"
	bsObj = BeautifulSoup(html,"lxml")
	for img in bsObj.findAll("img"):
		   img["alt"] = img["alt"].replace('[','【')
		   'href' in img.parent.attrs \
		and img["src"]!="" \
		and img["alt"]!="" \
		and	imgFetch( url["host"],img["src"] ) \
		and	dat.write(yml % (img["alt"],url["cloud"]+img["src"],img.parent.attrs['href']))
	dat.close()
	temp.close()


def run():
	try:
		html = urlopen(url['host']+url['forum'])
	except Exception as e:
		outlog(str(e))
	else:
		outdata(html.read())
	finally:
		swift()
		git()

run()
# for i in range(0,6*24):
# 	Timer(600*i, run ).start()
