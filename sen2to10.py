# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:56:01 2019

@author: Shengjie Liu
@Email: liushengjie0756@gmail.com
"""

import numpy as np
import gdal
import glob
import os
from scipy.ndimage import zoom
import argparse


def setGeo(geotransform,bgx,bgy,x_offset=0):
    if x_offset==0:
        x_offset = geotransform[1]
        y_offset = geotransform[5]
    else:
        x_offset = x_offset
        y_offset = -x_offset
    reset0 = geotransform[0] + bgx*geotransform[1]
    reset3 = geotransform[3] + bgy*geotransform[5]
    reset = (reset0,x_offset,geotransform[2],
             reset3,geotransform[4],y_offset)
    return reset


def sen20to10(fn,outdir=None):
    im = gdal.Open(fn,gdal.GA_ReadOnly)
    projection = im.GetProjection()
    geotransform = im.GetGeoTransform()
    im = im.ReadAsArray()
    newgeo = setGeo(geotransform,0,0,x_offset=10)
    im = zoom(im,[2,2],order=0,mode='nearest')
    imx,imy = im.shape
    
    name = fn[-11:-4]
    if outdir==None:
        name = wdir+'/'+name
    else:
        name = outdir+'/'+name
    print(name)
    outdata = gdal.GetDriverByName('GTiff').Create(name+'.tif',imy,imx,1,gdal.GDT_UInt16)
    outdata.SetGeoTransform(newgeo)
    outdata.SetProjection(projection)
    outdata.GetRasterBand(1).WriteArray(im)
    outdata.FlushCache() ##saves to disk!!
    outdata = None
    
    
def read_save(fn,outdir=None):
    im = gdal.Open(fn,gdal.GA_ReadOnly)
    projection = im.GetProjection()
    geotransform = im.GetGeoTransform()
    im = im.ReadAsArray()
    imx,imy = im.shape
    
    name = fn[-11:-4]
    if outdir==None:
        name = wdir+'/'+name
    else:
        name = outdir+'/'+name
    print(name)
    outdata = gdal.GetDriverByName('GTiff').Create(name+'.tif',imy,imx,1,gdal.GDT_UInt16)
    outdata.SetGeoTransform(geotransform)
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
                if '10m' in fn[-11:-4]:
                    read_save(fn,outdir=outdir)
                elif '20m' in fn[-11:-4]:
                    sen20to10(fn,outdir=outdir)
    return 0


def sen2cat(wdir,img='*.tif',name='concat',outdir=None):
    flist = glob.glob(wdir+'/'+img)
    imz = len(flist)
    count = 0
    
    if outdir==None:
        outdir = wdir
    name = outdir+'/'+name
        
    os.chdir(outdir)
    print(flist)
    for fn in flist:
#        print(fn)
        im = gdal.Open(fn,gdal.GA_ReadOnly)
        projection = im.GetProjection()
        geotransform = im.GetGeoTransform()
        im = im.ReadAsArray()
        imx,imy = im.shape

        count += 1
        
        if count==1:
            outdata = gdal.GetDriverByName('GTiff').Create(name+'.tif',imy,imx,imz,gdal.GDT_UInt16)
            outdata.SetGeoTransform(geotransform)
            outdata.SetProjection(projection)
        outdata.GetRasterBand(count).WriteArray(im)
        outdata.FlushCache() ##saves to disk!!
    outdata = None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--wdir', type=str, default=None)
    parser.add_argument('--outdir', type=str, default=None)
    parser.add_argument('--mode', type=str, default=None)
    args = parser.parse_args()
    wdir = args.wdir
    outdir = args.outdir
    mode = args.mode
#    print(mode)
    if mode in ['all','20']:
        pass
    else:
        mode = 'all'
        
    if outdir==None:
        outdir = wdir
        
    if wdir!=None:
        os.chdir(wdir)
        readjp2single(wdir,outdir=outdir,mode=mode)
        sen2cat(outdir)
    else:
        print('No directory specified!!')
    
    
