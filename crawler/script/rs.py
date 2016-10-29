#-*-coding:utf-8-*-
from urllib.request import urlopen
from urllib.request import urlretrieve
from threading import Timer  
from bs4 import BeautifulSoup
import os
import time
import re 

  

url = {
	"host": "http://rs.xidian.edu.cn/",
	"git": "../../",
	"forum": "forum.php?mod=forumdisplay&fid=106",
	"data": "_data/rs.yml",
	"temp": "img_template.txt",
	"log" : "git.log",
	"storage" : "../storage/",
	"cloud" :"/crawler/storage/"
}




def git():
	shell = [
		"git add .",
		"git commit -m 'send from my crawler' ",
		"git pull",
		"git merge",
		"git push "
	]
	gitResult=""
	for i in shell:
		gitResult += os.popen(i).read()
		# time.sleep( 5 )
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
	dat  = open(url["git"]+url["data"],"w+")
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
		git()

run()  
# for i in range(1,12*24*3):
# 	Timer(60*i, run ).start()   





