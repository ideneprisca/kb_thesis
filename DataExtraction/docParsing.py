import numpy as np
import xml.etree.cElementTree as Et
import re
from pathlib import Path
import string
import os

final = []
finalList=[]
character = "- "
characters_to_remove = "\\"

#xml textual file loading, parsing and cleaning xml file

def listdirs(rootdir):
    global finalList
    fullname = []
    complete_text= []
    for directory in Path(rootdir).iterdir():
        if directory.is_dir():
            for filename in os.listdir(directory):
                if not filename.endswith('.xml'): continue
                file = os.path.join(directory, filename)
                tree = Et.parse(file)
                records = tree.getroot()
                for record in records.findall('record'):
                    texte = record.find('page').text
                    fin = re.sub('\s{2,}', ' ', str(texte))
                    cleanText1 = fin.replace(character, "")
                    cleanText2 = cleanText1.replace(characters_to_remove, "")
                    res = cleanText2.count('..')
                    #if res < 50:
                    finalList.append(cleanText2)
    return finalList


if __name__ == "__main__":
 rootdir = 'C:/Users/user/Desktop/thesis/sestra/bo0144'
 #print("begin")
 res = listdirs(rootdir)
 #print(res)



#print("[".join(final))

#info_page = []
#for record in records.findall('record'):
    #cod_page = record.attrib.get("firstPageId")
    #title = record.find('title').text
    #texte = record.find('page').text
   # info_page.append(["cod_page:",cod_page,"title:",title,"texte:",texte])
    #print("cod_page:",cod_page)
    #print("title:",title)
  #  print("text:",texte)
#print(info_page)






