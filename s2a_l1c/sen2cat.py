# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:55:09 2019

@author: Shengjie Liu
@Email: liushengjie0756@gmail.com
"""

import gdal
import numpy as np
import glob

def sen2cat(wdir,img='*.tif',name='concat',outdir=None):
    if outdir==None:
        name = wdir+'/'+name
    else:
        name = outdir+'/'+name
        
    flist = glob.glob(wdir+'/'+img)
    imz = len(flist)
    count = 0
    
    for fn in flist:
        print(fn)
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