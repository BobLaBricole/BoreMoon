#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup

def extractMaree(nomFichier):
        path_html_maree = '../html/'
        html = open(path_html_maree+nomFichier,'r')
        soup = BeautifulSoup.BeautifulSoup(html,"html.parser")
        prev_tag_date=''
        tag_date=''
        key_date = 0
        cpt_pm_jour=0
        for m in soup.find_all('li', class_='selected'):
                tag_mois = m.get_text()
                print(tag_mois)


        for pm in soup.find_all('div',class_='pleine_mer'):
                prev_tag_date=tag_date
                tag_date = pm.find_previous(class_='tab_date')
                coef = pm.find_next(class_='cercle')
                #gestion du compteur de pm par jour
                #si on est sur la 2 eme pleine mer pour le meme jour on prend le coef suivant"
                if prev_tag_date==tag_date :
                        coef = coef.find_next(class_='cercle')
                        cpt_pm_jour = 2
                else :
                        cpt_pm_jour = 1
                        
                val_coef = coef.get_text()
                if int(val_coef) > 80 :
                        lbl_maree =tag_date.get_text() +' '+ tag_mois +' - ' + pm.get_text() +'-'+ pm.next_sibling.next_sibling.get_text() +'-coef : ' + val_coef
                        print(lbl_maree)	


                                #else :
                                        #continue
                                        #tag_date = p.parent.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.find('div',class_='tab_date').get_text()
                                #prev_tag_date = tag_date	
                                
                                #print(tags_PM[key_date].get_text()+' '+tags_PM[key_date].next_sibling.next_sibling.get_text())
        #f = open('soup.html','w')
        #f.write(html.decode(encoding="utf-8", errors="ignore"))
        #f.close() 
