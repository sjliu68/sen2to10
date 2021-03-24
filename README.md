# sen2to10
Convert Sentinel-2 imagery to spatial resolution of 10 m.

# Overview
This repo aims to convert Sentinel-2 imagery to spatial resolution of 10 m for further processing.

Feel free to contact me: liushengjie0756 [AT] gmail.com

## How to use
### python sen2to10.py --wdir=imageDir --outdir=saveDir
##### Read the 'jp2' images in 'F:\data' and subdirectories, and then convert them to 10 m GSD and save them in 'F:\data0603'
    python sen2to10.py --wdir=F:\data --outdir=F:\data0603


## Features
- You can choose to convert 20 m bands only or both 10 and 20 m bands
- You can import each function individually to your scripts


## Updates
- [x] Merge images to a single tif


## To do
- [ ] Subset function

## Issues
Mar 24, 2021: If you encounter "ERROR 1: PROJ: proj_create_from_database: Cannot find proj.db", please downgrade gdal to version 2.4.1. Or try to set the environment variable manually based on discussion on [stackoverflow](https://gis.stackexchange.com/questions/326968/ogr2ogr-error-1-proj-pj-obj-create-cannot-find-proj-db) or [the gdal repo](https://github.com/PDAL/PDAL/issues/2544).
