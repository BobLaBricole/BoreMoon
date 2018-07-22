#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup
from MareeMascaretExtract import *
def extractHTML2File(adrWeb,nomFichier ):
        for i in range(12):
                #url= "%s%s%s" % ("http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-", i,".php")
                url= "%s%s%s" % (adrWeb, i,".php")
                print(url)
                #html = request.urlopen('http://marine.meteoconsult.fr/meteo-marine/horaires-maree-libourne-1046-0.php').read()
                html = request.urlopen(url).read()
                Request(
                #namefile = "%s%s-%s.html" % ("../html/","maree-libourne", i)
                namefile = "%s%s-%s.html" % ("../html/",nomFichier, i)
                print(namefile)
                soup = BeautifulSoup.BeautifulSoup(html.decode('utf-8', 'ignore'),"html.parser")
                f = open(namefile,'w')
                f.write(html.decode(encoding="utf-8", errors="ignore"))
                f.close()
                extractMaree(namefile)
##Accept: */*
##Origin: http://maree.shom.fr
##Referer: http://maree.shom.fr/harbor/PORT-BLOC/hlt/0?date=2018-07-8&utc=standard
##User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
##
##hack -> utiliser ce ws (avec header du dessus) : https://services.data.shom.fr/b2q8lrcdl4s04cbabsj4nhcb/hdm/spm/hlt?harborName=PORT-BLOC&duration=7&date=2018-07-8&utc=standard&correlation=1
##avec b2q8lrcdl4s04cbabsj4nhcb la clé se trouvant derrière la 6 eme occurence de //services.data.shom.fr/ dans l'attribut "content" de la balise <meta name="shom-horaires-des-marees/config/environment"
