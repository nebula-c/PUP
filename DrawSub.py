#!/usr/bin/env python3

import os,sys
import argparse
import time 
import numpy as np

start = time.time()

# import sub


parser=argparse.ArgumentParser(description='Submission program for Carrier Board Test')
parser.add_argument('-o','--order',action='store_true',help='Show order of image(imglist.txt)')
parser.add_argument('-n','--number',type=int, help='Number of image(imglist.txt)')
parser.add_argument('--name', help='Set imagefile name(if you need)')

args=parser.parse_args()


imglistfilepath = "./imglist.txt"
imglistfile = open(imglistfilepath, 'r')
imglist = imglistfile.read()    
imglist = imglist.strip()

cmdlistfilepath = "./cmdlist.txt"
cmdlistfile = open(cmdlistfilepath, 'r')
cmdlist = cmdlistfile.read()    
cmdlist = cmdlist.strip()


if args.order:    
    print(imglist)
    
if args.number:
    inputnum = args.number
    imglist = imglist.split("\n")
    imgpath = None
    
    isfirst=True
    for imgline in imglist:
        if isfirst==True:
            isfirst=False
            continue
        imgnum = imgline.split(",")[0].strip()
        
        if int(imgnum) == inputnum:
            imgpath = imgline.split(",")[1].strip()

    
    cmdlist = cmdlist.split("\n")
    isfirst=True
    for cmdline in cmdlist:
        if isfirst==True:
            isfirst=False
            continue
        cmdnum = cmdline.split(",")[0].strip()
        
        if int(cmdnum) == inputnum:
            mycmd = cmdline.split(",")[1].strip()
        
    maincmd = mycmd + ' ' + imgpath
    os.system(maincmd)
    
    
    
    
end = time.time()
print("=========================================")
print("Run-time(DrawSub) : {0:00.2f} sec(sub)".format(end-start))
print("=========================================")
