from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
url = {
	"git": "../../",
	"rs": "http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=106",
	"data": "_data/rs.yml",
	"temp": "img_template.txt"
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
	"sudo git -C %s add .",
	"sudo git -C %s commit -m 'send from my crawler' ",
	"sudo git -C %s push "
]
for i in shell:
	str = os.system(i % url["git"])
	print(str)
