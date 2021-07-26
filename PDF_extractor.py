import cv2 as cv
import imutils
import numpy as np
import os
from pdf2image import convert_from_path
from extract import extract
os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Saves")
lastpg=83
firstpg=83
lis=convert_from_path(pdf_path="C:/Users/suhaa/Desktop/Books/Hobbies/My_system.pdf",last_page=lastpg,first_page=firstpg,poppler_path=r"C:\0 My programs\poppler-0.68.0_x86\poppler-0.68.0\bin")
for i in range(len(lis)):
    lis[i].save("holder.jpeg", "JPEG")
    image = cv.imread("holder.jpeg")
    extract(image,firstpg+i)
