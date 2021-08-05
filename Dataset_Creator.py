#save data in file
#check file for data
#continue post end
#an app for classification data generation(connecting clients and shit-bored users)


#GAMEDEV
#make a screen
#define blocks of choices and the return values triggered using mouse clicks
#link with pdf_extractor using a generator

import cv2 as cv

import imutils
import numpy as np
import os
from pdf2image import convert_from_path
from extract import extract
from extract_piece import extract_piece
useless_var=0

def get_max_name():     # finds what to name saved img to not mess up previously saved images
    lis=os.listdir(path=r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Pieces")
    max=-1
    lis.remove("holder.jpeg")
    for imgname in lis:
        imgname = imgname.strip(".png")
        les = imgname.split("_")[0]
        max = int(les) if max < int(les) else max
    return max



count=0
os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Pieces")
lastpg=100
firstpg=100
#"C:/Users/suhaa/Desktop/Books/Hobbies/My_system.pdf"
lis=convert_from_path(pdf_path="C:/Users/suhaa/Desktop/Books/Hobbies/My_system.pdf",last_page=lastpg,first_page=firstpg,poppler_path=r"C:\0 My programs\poppler-0.68.0_x86\poppler-0.68.0\bin")
for i in range(len(lis)):
    print(1)
    lis[i].save("holder.jpeg", "JPEG")
    image = cv.imread("holder.jpeg",)
    itera=extract_piece(image,firstpg+i)
    while True:
        try:
            useless_var+=1      #count number of images to help us find images to separate
            out_img = next(itera)
            cv.imwrite(str(count)+r".png",out_img)
            count+=1
        except StopIteration:
            break
print(get_max_name(),get_max_name()-useless_var+1)
