#This code has been designed for Dfab.Studio by Kevin O'Neill - French Mechatronics Engineer student at ENSIBS Lorient

import requests
import json
from pprint import pprint
import os
import time
import shutil,sys
import serial

port = 'COM5'

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Valetta,MT&appid=77a9c4104f54722fbbeb8c6048122c56")
data=r.json()
a=json.dumps(data, indent=4)
pprint(data)

#Ecriture
f = open("Data.txt", "w")
f.write(a)
f.close()


#===========================Temperature=========================
chaine = "temp\""
temp=""
f = open("Data.txt","r")
for ligne in f:
    if chaine in ligne:
        temp=ligne
f.close()
a=0
i=0
j=0
val=[]
l=len(temp)

while i < l:
    if temp[i]=="." or temp[i]=="0" or temp[i]=="1" or temp[i] == "2" or temp[i]=="3" or temp[i] == "4" or temp[i] == "5" or temp[i] == "6" or temp[i] == "7" or temp[i] == "8" or temp[i] == "9":
        val.append(temp[i])
        j+=1
    i += 1
V2=[]
i=0
while i < j:
    if val[i]=="0":
        V2.append(0)
    if val[i]=="1":
        V2.append(1)
    if val[i]=="2":
        V2.append(2)
    if val[i]=="3":
        V2.append(3)
    if val[i]=="4":
        V2.append(4)
    if val[i]=="5":
        V2.append(5)
    if val[i]=="6":
        V2.append(6)
    if val[i]=="7":
        V2.append(7)
    if val[i]=="8":
        V2.append(8)
    if val[i]=="9":
        V2.append(9)
    i+=1

print
a=(100*V2[0])+(10*V2[1])+V2[2]+(0.1*V2[3])+(0.01*V2[4])
print"Kelvin Temperature : ",a
temp=a-273.15
print"Celcius Temperature : ",temp
tp= str(temp)

#=========================Description===================
chaine = "description"
des=""
f = open("Data.txt","r")
for ligne in f:
    if chaine in ligne:
        des=ligne
f.close()
IC=""
i=0
j=0
des2=[]
l=len(des)
n=0
while i < l:
    if des[i]=="\"" :
        n+=1
    if n==3:
        i += 1
        n=4
    if n==4:
        des2.append(des[i])
        j+=1
    i += 1

i=0
while i<j:
    IC=IC+des2[i]
    i+=1
print"Description : ",IC

#=====================Icon choice =====================
GCodeWeather=""
if IC=="clear sky":
    GCodeWeather="sunny.cnc"
if IC=="few clouds":
     GCodeWeather="coversun.cnc"
if IC=="scattered clouds" or IC=="broken clouds":
    GCodeWeather="cover.cnc"
if IC=="shower rain":
    GCodeWeather="coverrainny.cnc"
if IC=="rain":
    GCodeWeather="rain.cnc"
if IC=="thunderstorm":
     GCodeWeather="storm.cnc"
if IC=="snow":
    GCodeWeather="snow.cnc"
if IC=="mist":
    GCodeWeather="mist.cnc"

print"Val de GCW : ",GCodeWeather

#=====================Digits choice =====================
if tp[0]=="-":
    DG1=tp[1]+".cnc"
    DG2="A"+tp[2]+".cnc"
    minus=1
if tp[0]!="-":
    DG1=tp[0]+".cnc"
    DG2="A"+tp[1]+".cnc"
    minus=0

print"Val du minus :",minus
print"DG1=",DG1
print"DG2=",DG2

#=====================Making 1 File =====================
a="Texte1.txt"
b="Texte2.txt"
fichier = open(GCodeWeather, "r")
fichier = open(DG1, "r")
fichier = open(DG2, "r")
fichier = open("c.cnc", "r")
fichier = open("Final.cnc", "w")
shutil.copyfileobj(open(GCodeWeather, 'r'), fichier)
if minus==1:
    shutil.copyfileobj(open("minus.cnc", 'r'), fichier)
shutil.copyfileobj(open(DG1, 'r'), fichier)
shutil.copyfileobj(open(DG2, 'r'), fichier)
shutil.copyfileobj(open("c.cnc", 'r'), fichier)
fichier.close()

#=====================Drawing =====================
s = serial.Serial(port,115200)
f = open("Final.cnc","r")
time.sleep(2) 
s.flushInput() 
for line in f:
    l = line.strip()
    print ('Sending: ' + l)
    s.write(bytes (l + '\n'))
    grbl_out = s.readline() 
    print (' : ' + grbl_out.strip())
f.close()
s.close()
print "Done !"
