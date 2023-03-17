#!/usr/bin/env python3

#---------------------------------------------------------------------
# Core code for PUP
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

import sys
import os
import itertools
import copy
import pickle

class pup:
    mycont = ''
    myfig = ''
    myax = ''
    mycmap = 'viridis'
    myinterpolation = 'none'
    myim = ''
    mythrs = ''
    mycbar = ''
    mydpi = 300
    
    def testfunc(self,):
        print("")
        print(".........................................................................")
        print("    Hello, this is result of test function of core.py at PUP/src/    ")
        print(".........................................................................")
        print("")
        
    def SetPLT(self,xsize,ysize,myfacecolor='white'):
        self.myfig = plt.figure(1,figsize=(xsize,ysize),facecolor=myfacecolor)
        self.myax = plt.axes()
    
    def loadpkl(self,mypath):
        with open(mypath,'rb') as myfile:
            mydata = pickle.load(myfile)
        self.mycont = mydata['img']
    
    def showImg(self,):
        self.myim = plt.imshow(self.mycont,cmap=self.mycmap,interpolation=self.myinterpolation)
        
    def ShowPLT(self,):
        plt.show()
        
    ### Title and X&Y labels
    def SetTL(self,mytitle,myxlabel,myylabel):
        plt.title(mytitle)
        plt.xlabel(myxlabel)
        plt.ylabel(myylabel)
    
    def SetCbar(self,):
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(self.myax)
        width = axes_size.AxesY(self.myax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        self.mycbar = plt.colorbar(self.myim,cax=cax)
        # plt.clim(-30,30)
        # plt.clim(0,30)
    
    def SetLim(self,whichaxis,lowlim,highlim):
        if whichaxis == 'x':
            plt.xlim(lowlim,highlim)
        if whichaxis == 'y':
            plt.xlim(lowlim,highlim)
        if whichaxis == 'z' or whichaxis == 'c':
            plt.clim(lowlim,highlim)
            
    def SetTheme(self,mytheme):
        self.mycmap = copy.copy(plt.cm.get_cmap(mytheme))
    
    ### Set interpolation option. default:none
    def SetInterpolation(self,myopt):
        self.myinterpolation = myopt
    
    def SetUnderWhite(self,mycolor='white'):
        self.mycmap.set_under(color=mycolor)
        
    def SetZlabel(self,mylabel):
        self.mycbar.set_label(mylabel)
    
    def SavePLT(self,myfilename):
        plt.savefig(myfilename,dpi=self.mydpi)
        
    def SetDPI(self,mydpi):
        self.mydpi = mydpi