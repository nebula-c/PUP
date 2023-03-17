#!/usr/bin/env python3

#---------------------------------------------------------------------
# Painter Using Pickle
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

import os, sys
import argparse
import time
# import itertools
import copy
import pickle
from src import core

start = time.time()  # To measure runtime for pup

### ===================================================================
### Parser part

parser=argparse.ArgumentParser(description='Submission program for Carrier Board Test')
parser.add_argument('--input','-i',help='input data path')
parser.add_argument('--filename','-n',help='Output file name')
parser.add_argument('--xlow', '-xl',type=float,help='Set low limit value for X axis')
parser.add_argument('--xhigh','-xh',type=float,help='Set high limit value for X axis')
parser.add_argument('--ylow', '-yl',type=float,help='Set low limit value for Y axis')
parser.add_argument('--yhigh','-yh',type=float,help='Set high limit value for Y axis')
parser.add_argument('--zlow', '-zl',type=float,help='Set low limit value for Z axis')
parser.add_argument('--zhigh','-zh',type=float,help='Set high limit value for Z axis')
parser.add_argument('--title','-t',help='Title',default='')
parser.add_argument('--xlabel','-x',help='X-Label',default='')
parser.add_argument('--ylabel','-y',help='Y-Label',default='')
parser.add_argument('--zlabel','-z',help='Z-Label',default='')
parser.add_argument('--pltx','-px',help='Set x size for plt(default:7)',default=7)
parser.add_argument('--plty','-py',help='Set y size for plt(default:9)',default=9)
parser.add_argument('--theme',help='Theme for color map',default='viridis')
parser.add_argument('--underwhite','-w',action='store_true',help='Set under value as 0',default=True)
parser.add_argument('--colormap','-c',action='store_true',help='For colormap')
parser.add_argument('--show','-s',action='store_true',help='Show plt window')
parser.add_argument('--file','-f',action='store_true',help='Save as png')
parser.add_argument('--path','-p',help='Output file path',default='.')
args=parser.parse_args()
### ===================================================================



### ===================================================================
### Object declaration & test
pup = core.pup()
# pup.testfunc()
### ===================================================================



### ===================================================================
### Load pkl data
if not args.input :
    print("Please insert input data")
pup.loadpkl(args.input)
### ===================================================================



# ### ===================================================================
# ### Main part(Hard coding)
# pup.SetPLT(7,9)
# pup.SetTL("testtitle","Column","Row")
# pup.SetTheme("viridis")
# pup.SetUnderWhite()
# pup.showImg()
# pup.SetCbar()
# pup.SetLim('z',0.5,4)
# pup.SetZlabel("hit")
# ### ===================================================================


### ===================================================================
### Main part(soft coding)
pup.SetPLT(args.pltx,args.plty)
pup.SetTL(args.title,args.xlabel,args.ylabel)
if args.colormap:
    pup.SetTheme(args.theme)
    if args.underwhite:
        pup.SetUnderWhite()
pup.showImg()
if args.colormap:
    pup.SetCbar()
if (not args.zlow == None) and (not args.zhigh == None):
    pup.SetLim('z',args.zlow,args.zhigh)
### ===================================================================



### ===================================================================
### Output part
if args.show:
    pup.ShowPLT()
if args.file:
    pup.SavePLT(args.path + '/' + args.filename)
### ===================================================================



if __name__ == "__main__":
    end = time.time()
    print("=========================================")
    print("Run-time(pup.py) : {0:00.2f} sec(sub)".format(end-start))
    print("=========================================")