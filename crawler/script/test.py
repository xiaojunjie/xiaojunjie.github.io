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
	outlog(gitResult)

def imgFetch(host,src):
	imgDirname = os.path.dirname(url["storage"]+src)
	os.path.exists(imgDirname) or os.makedirs(imgDirname)
	urlretrieve(host+src, url["storage"]+src)

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
		if 'href' in img.parent.attrs and img["src"]!="" and img["alt"]!="":
			imgFetch( url["host"],img["src"] )
			dat.write(yml % (img["alt"],url["cloud"]+img["src"],img.parent.attrs['href']))
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

  
for i in range(1,12*24*3):
	Timer(60*i, run ).start()   





