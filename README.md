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
Mar 24, 2021: If you encounter "ERROR 1: PROJ: proj_create_from_database: Cannot find proj.db", please downgrade gdal to version 2.4.1. Or try to [set the environment variable mannualy](https://stackoverflow.com/questions/56764046/gdal-ogr2ogr-cannot-find-proj-db-error#:~:text=You%20might%20need%20to%20set%20the%20PROJ_LIB%20environment%20variable.&text=If%20you%20don't%20find,see%20if%20things%20start%20working).
