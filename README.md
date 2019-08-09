# sen2to10
Convert Sentinel-2 imagery to spatial resolution of 10 m.

# Overview
This repo aims to convert Sentinel-2 imagery to spatial resolution of 10 m for further processing.

Feel free to contact me: liushengjie0756 [AT] gmail.com

# How to use
## python sen2to10.py --wdir=imageDir --outdir=saveDir
##### Read the 'jp2' images in 'F:\data' and subdirectories, and then convert them to 10 m GSD and save them in 'F:\data0603'
    python sen2to10.py --wdir=F:\data --outdir=F:\data0603


## Features
- You can choose to convert 20 m bands only or both 10 and 20 m bands
- You can import each function individually to your scripts


## To do
- Convert the images to a single file
- Subset function
