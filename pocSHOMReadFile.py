#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup
for i in range(1,31,7):
	#url= "%s%s%s" % ("http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-", i,".php")
	url="%s%s%s" % ("http://maree.shom.fr/harbor/PORT-BLOC/hlt/0?date=2018-07-",i,"&utc=standard")
	print(url)
	#html = request.urlopen('http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-0.php').read()
	html = request.urlopen(url).read()
	namefile = "%s%s-%s.html" % ("./html/","maree-shom-portbloc", i)
	print(namefile)
	soup = BeautifulSoup.BeautifulSoup(html.decode('utf-8', 'ignore'),"html.parser")
	f = open(namefile,'w')
	f.write(html.decode(encoding="utf-8", errors="ignore"))
	f.close()
	
