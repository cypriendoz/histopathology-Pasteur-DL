import os
from os import listdir
from os.path import isfile, join

import openslide
import numpy as np
from  matplotlib import pyplot as plt
import os

from lxml import etree

from matplotlib import path # to use contains.point instead of point_in_poly

Epfolder = "/pasteur/projets/policy01/Imod-grenier/cdoz/histopathology/Ependymomes_ann"
Glfolder = "/pasteur/projets/policy01/Imod-grenier/cdoz/histopathology/Gliomes_4_ann"

Ependndpi = [f for f in listdir(Epfolder)if f.endswith(".ndpi")] #if not f.startswith('.') : #if f != '.DS_Store'this way you filter out all "hidden" files
Gliomendpi = [f for f in listdir(Glfolder)if f.endswith(".ndpi")]
Ependndpa = [f for f in listdir(Epfolder)if f.endswith(".ndpa")]
Gliomendpa = [f for f in listdir(Glfolder)if f.endswith(".ndpa")]


os.chdir(Epfolder)

for slide in Ependndpi:
    s =openslide.open_slide(slide)
    totalsize = s.level_dimensions[0]
    print('the totalsize of '+slide+' is '+str(totalsize))

os.chdir(Glfolder)

for slide in Gliomendpi:
    s =openslide.open_slide(slide)
    totalsize = s.level_dimensions[0]
    print('the totalsize of '+slide+' is '+str(totalsize))





"""
slide1 = Ependndpi[0]
slide2 = Ependndpi[1]



s1 = openslide.open_slide(slide1)
s2 = openslide.open_slide(slide2)
s2.get_thumbnail((1000,1000))
s1.level_downsamples
s2.level_dimensions


slide.read_region((50000,12320),2,(150,150))
"""
