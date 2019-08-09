# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:56:01 2019

@author: Administrator
"""

import numpy as np
import gdal
import glob
import os
from scipy.ndimage import zoom
import argparse

def setGeo(geotransform,bgx,bgy,imx=0):
    if imx==0:
        imx = geotransform[1]
        imy = geotransform[5]
    else:
        imx = imx
        imy = -imx
    reset0 = geotransform[0] + bgx*imx
    reset3 = geotransform[3] + bgy*imy
    reset = (reset0,imx,geotransform[2],
             reset3,geotransform[4],imy)
    return reset

def sen20to10(fn,outdir=None):
    im = gdal.Open(fn,gdal.GA_ReadOnly)
    projection = im.GetProjection()
    geotransform = im.GetGeoTransform()
    im = im.ReadAsArray()
    newgeo = setGeo(geotransform,0,0,imx=10)
    im = zoom(im,[2,2],order=0,mode='nearest')
    imx,imy = im.shape
    
    name = fn[-11:-4]
    if outdir==None:
        pass
    else:
        name = outdir+'/'+name
    print(name)
    outdata = gdal.GetDriverByName('GTiff').Create(name+'.tif', imy, imx, 1, gdal.GDT_UInt16)
    outdata.SetGeoTransform(newgeo)
    outdata.SetProjection(projection)
    outdata.GetRasterBand(1).WriteArray(im)
    outdata.FlushCache() ##saves to disk!!
    outdata = None

def readjp2single(fp,outdir=None,mode='20'):
    if mode=='20':
        ls = ['B05_20m','B06_20m','B07_20m','B8A_20m','B11_20m','B12_20m']
    elif mode=='all':
        ls = ['B02_10m','B03_10m','B04_10m','B08_10m',
              'B05_20m','B06_20m','B07_20m','B8A_20m','B11_20m','B12_20m']
    else:
        print('mode?')
    for fn in glob.glob(fp+os.sep+'*'):
        if os.path.isdir(fn):
            readjp2single(fn,outdir=outdir,mode=mode)
        else:
            if fn[-11:-4] in ls:
                sen20to10(fn,outdir=outdir)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--wdir', type=str, default=None)
    parser.add_argument('--outdir', type=str, default=None)
    args = parser.parse_args()
    wdir = args.wdir
    outdir = args.outdir
    
    if wdir!=None:
        readjp2single(wdir,outdir=outdir,mode='20')
    else:
        print('No directory specified!!')
    
    
