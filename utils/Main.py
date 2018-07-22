#prog poue extract html + extract maree
from MareeMascaretExtract import *
from MeteoConsultExtract import *
nomFichier="maree-port-bloc"
extractHTML2File("http://marine.meteoconsult.fr/meteo-marine/horaires-maree-port-bloc-59-",nomFichier )
