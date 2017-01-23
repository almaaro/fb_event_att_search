# -*- coding: cp1252 -*-H
'''
Created on 15.4.2016

@author: Alvar
'''
import urllib.request
import re
token_file = open("token", "r")
token = token_file.read().strip()
html=open("kuvat.html", "w")
html.write("<html>")
name = input("Nimi: ")
opener=urllib.request.build_opener()
for n in ["attending","maybe","noreply"]:
    try:
        link="https://graph.facebook.com/v2.6/1042575692444175/"+n+"?access_token="+token
        while True:
            src=opener.open(link).read().decode("utf-8")
            names=re.findall('(?<="name":")(.*?)(?=")',src)
            ids=re.findall('(?<="id":")(.*?)(?=")',src)
            for i in range(len(names)):
                if(names[i].startswith(name)):
                    print(names[i])
                    html.write("<br><br>"+names[i]+"<br><img src='https://graph.facebook.com/v2.6/"+ids[i]+"/picture?type=large&access_token="+token+"'>")
            link=re.search('(?<="next":")(.*?)(?=")',src).group()
            link=link.replace("\\", "")
    except :
        print("\n"+n+" done.\n")
html.write("</html>")
html.close()
