#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup
for i in range(5):
	#html = request.urlopen('http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-0.php').read()
#soup = BeautifulSoup.BeautifulSoup(html.read().decode('utf-8', 'ignore'))
#print(html) 
	namfile = "%s %s" % (maree-libourne, i)
#f = open('maree-libourne.html','w')
#f.write(html.decode(encoding="utf-8", errors="ignore"))
#f.close() 