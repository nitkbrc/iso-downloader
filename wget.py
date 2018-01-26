# ****** B R Chandavarkar Modifications ******



# */10 * * * * python /etc/cron.hourly/wget.py

# Phyton script to download updated Ubuntu's *.iso. 
# Created by:
# CSE Dept., NITK, Surathkal
# email: 
# Date: 14.01.2018

import os,re

# Reading the old md5 value of .iso files

path = "/home/swapnil/Desktop/U_Mirror/versions/17/MD5SUMS"
l=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l.append(word)   

old = l[0]

# Downloading the new md5 value of .iso files

os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P /home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM/")

path1 = "/home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM/MD5SUMS"
l1=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l1.append(word)   

newm = l1[0]


os.system("openssl dgst -md5 /home/swapnil/Desktop/U_Mirror/versions/17/ubuntu-17.10-desktop-amd64.iso > /home/swapnil/Desktop/U_Mirror/versions/17/MD5_cross_check.txt")


with open("/home/swapnil/Desktop/U_Mirror/versions/17/MD5_cross_check.txt",'r') as f:
	md  = f.readline() 

l2=[]	
for parts in md.split("= "):
	l2.append(parts)

md = l2[1]
#print old
#print newm
#print md

if old != newm and old != md :
	os.system("wget http://releases.ubuntu.com/17.10/ubuntu-17.10-desktop-amd64.iso -P /home/swapnil/Desktop/U_Mirror/versions/")
	os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P /home/swapnil/Desktop/U_Mirror/versions/17/")


