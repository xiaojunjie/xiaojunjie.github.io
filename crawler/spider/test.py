from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time
url = {
	"git": "../../",
	"rs": "http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=106",
	"data": "_data/rs.yml",
	"temp": "img_template.txt",
	"log" : "git.log",
	"img" : "../img"
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
			dat.write(yml % (img["alt"],img["src"],img.parent.attrs['href']))
	dat.close() 
	temp.close()

try:
	html = urlopen(url['rs'])
except Exception as e:
	outlog(e)
else:
	outdata(html.read())
finally:
	git()





