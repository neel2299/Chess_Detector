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
count=0
os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Pieces")
lastpg=49
firstpg=49
lis=convert_from_path(pdf_path="C:/Users/suhaa/Desktop/Books/Hobbies/My_system.pdf",last_page=lastpg,first_page=firstpg,poppler_path=r"C:\0 My programs\poppler-0.68.0_x86\poppler-0.68.0\bin")
for i in range(len(lis)):
    lis[i].save("holder.jpeg", "JPEG")
    image = cv.imread("holder.jpeg",)
    itera=extract_piece(image,firstpg+i)
    while True:
        try:
            out_img = next(itera)
            cv.imwrite(str(count)+r".jpeg",out_img)
            print(1)
            count+=1
        except StopIteration:
            break

