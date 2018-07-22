#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup, sys
print ("--------sys.argv[1] = %s " % sys.argv[1])

def extractHTML2File():
        for i in range(12):
                url= "%s%s%s" % ("http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-", i,".php")
                print(url)
                #html = request.urlopen('http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-0.php').read()
                html = request.urlopen(url).read()
                namefile = "%s%s-%s.html" % ("../html/","maree-libourne", i)
                print(namefile)
                soup = BeautifulSoup.BeautifulSoup(html.decode('utf-8', 'ignore'))
                f = open(namefile,'w')
                f.write(html.decode(encoding="utf-8", errors="ignore"))
                f.close()
