import openslide
import numpy as np
import os
#from __future__ import print_function


from os import listdir
from os.path import isfile, join #this is for the constrction of the list of files
from lxml import etree






def randomSampleSlide(slide, level=0, sampleNum=100, sampleSize=(512,512), stdThreshold=20, meanThreshold=220, maxFail=100):
    refDim = slide.level_dimensions[0]
    curDim = slide.level_dimensions[level]
    relativeSampleSize = (refDim[0]/curDim[0]*sampleSize[0], refDim[1]/curDim[1]*sampleSize[1])
    count = 0
    imgDict = {}
    #imgSave = [] #cyprien added this
    failed = 0
    while len(imgDict)<sampleNum:
        offset0 = int(np.random.uniform(0,refDim[0]-relativeSampleSize[0],1))
        offset1 = int(np.random.uniform(0,refDim[1]-relativeSampleSize[1],1))
        img = slide.read_region((offset0,offset1),level,sampleSize)
        aimg = np.array(img)
        failed +=1
        if failed>maxFail:
            raise Exception('failed to get a region too many times')
        #print('.', end="")
        if aimg.std()>stdThreshold and aimg.mean()< meanThreshold:
            failed = 0
            #print(':')#, end="")
            count+=1
            imgDict[(offset0, offset1)]= img
            #imgSave.extend(img) #cyprien added this
    #print('|',end=" ")

    if sampleNum ==1:
        return (offset0, offset1), img
    else:
        return imgDict



""" Example of use below

import contain # not sufficient
from contain import * # better

level=1
sampleNum=100
sampleSize = (512,512)
s0=sampleSize[0]
s1=sampleSize[1] #to access corners
lv=str(level)
dim=str(sampleSize)

os.chdir("/pasteur/projets/policy01/Imod-grenier/cdoz/histopathology/Gliomes_4_ann")

ndpa= "_14R00434 HE EXT - 2014-11-21 12.49.23.ndpi.ndpa"
f= "_14R00434 HE EXT - 2014-11-21 12.49.23.ndpi"

tree = etree.parse(ndpa)
annotations = tree.xpath('/annotations/ndpviewstate/annotation')
ANNOTATIONS=[] #annotations on a image ; on one images list for all the annotations
for annotation in annotations:
    POLYGON=[] #list of the coordinates of one polygon
    if annotation.attrib['color']=='#000000':
        pointlist=annotation[2]
        for point in pointlist:
            POLYGON.append((int(point[0].text),int(point[1].text)))
        ANNOTATIONS.append(POLYGON)


s = openslide.open_slide(f)
imgDict = randomSampleSlide(s,level=level, sampleNum=sampleNum)
for k in imgDict:
    #c ici que ca va se jouer si k est dans la zone
    K=str(k)
    #coord=str(coord)
    #print(I)
    #print(K)
    #print(coord)
    #pixels_inside=0
    #for P in ANNOTATIONS: #make the test for all the different polygon
        #if inside_polygon(k[0],k[1],P) : #(inside_polygon(k[0]-s0/2,k[1]-s1/2,P) and inside_polygon(k[0]+s0/2,k[1]-s1/2,P) and inside_polygon(k[0]-s0/2,k[1]+s1/2,P) and inside_polygon(k[0]+s0/2,k[1]+s1/2,P)):
    imgDict[k].save('/pasteur/projets/policy01/Imod-grenier/cdoz/histopathology/random_sample_test/level-'+lv+'_sampleSize-'+dim+'_slide-'+f+K+'.png')





#img.save('/home/cyprien/brain_tumor_randomSample/region.png')


"""
