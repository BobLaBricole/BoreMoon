#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib  import request
import bs4 as BeautifulSoup
path_html_maree = '../html/'
html = open(path_html_maree+'maree-libourne-0.html','r')
soup = BeautifulSoup.BeautifulSoup(html,"html.parser")
prev_tag_date=''
tag_date=''
key_date = 0
for m in soup.find_all('li', class_='selected'):
	tag_mois = m.get_text()
	print(tag_mois)

for p in soup.find_all('div', class_='cercle'):
	tag_coef=p.get_text()
	if p.get_text() !='':
		if int(p.get_text()) > 80 :
			#print("#############################")
			#print(tag_coef +' prev_tag_date-->'+ prev_tag_date)
			#print(tag_coef )
			#parents=p.find_parents("div",class_="heure")
			parents=p.find_previous_sibling()
			tag_date = p.parent.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.find('div',class_='tab_date').get_text()
			if prev_tag_date == tag_date :
				key_date = 1
			else :
				key_date = 0
				#print(prev_tag_date)
				#print(tag_date)
				#for tag_PM in p.parent.parent.previous_sibling.previous_sibling.find_all('div',class_='pleine_mer') :				
				#	print(tag_PM.get_text()+' '+tag_PM.next_sibling.next_sibling.get_text())
			tags_PM = p.parent.parent.previous_sibling.previous_sibling.find_all('div',class_='pleine_mer') 
			if  (len(tags_PM)==2 and  key_date == 1) or (len(tags_PM)==1 and  key_date == 0):
				lbl_maree = tag_date +' '+tag_mois+ ' ' + tags_PM[key_date].get_text()+' '+tags_PM[key_date].next_sibling.next_sibling.get_text()+' - coef ' + tag_coef
				print(lbl_maree)
			else :
				continue
				tag_date = p.parent.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.find('div',class_='tab_date').get_text()
			prev_tag_date = tag_date	
			
			#print(tags_PM[key_date].get_text()+' '+tags_PM[key_date].next_sibling.next_sibling.get_text())
#f = open('soup.html','w')
#f.write(html.decode(encoding="utf-8", errors="ignore"))
#f.close() 