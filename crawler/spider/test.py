from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
url = {
	"git": "../../",
	"rs": "http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=106",
	"data": "_data/rs.yml",
	"temp": "img_template.txt",
	"log" : "git.log"
}

temp = open(url["temp"],"r")
yml  = str(temp.read())+"\r\n\r\n"
dat  = open(url["git"]+url["data"],"w+") 
try:
	html = urlopen(url['rs'])
except Exception as e:
	print(e)
else:
	bsObj = BeautifulSoup(html.read(),"lxml")
	# print(bsObj.findAll(id="portal_block_343"));
	for img in bsObj.findAll("img"):
		if 'href' in img.parent.attrs and img["src"]!="" and img["alt"]!="":
			dat.write(yml % (img["alt"],img["src"],img.parent.attrs['href']))
finally:
	pass

dat.close()
temp.close()
shell = [
	"git add .",
	"git commit -m 'send from my crawler' ",
	"git pull",
	"git merge",
	"git push "
]
shellout = ""
for i in shell:
	shellout += os.popen(i).read()
log = open(url["log"],"a+")
log.write(shellout)
log.close()
