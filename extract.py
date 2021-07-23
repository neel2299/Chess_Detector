import cv2 as cv
import imutils
import os
image=cv.imread("Docu.jpeg")
image=imutils.resize(image,height=400,width=400)
def extract(image,page):
    img = cv.Canny(image, 2, 10)
    #cv.imshow("sh", img)
    croppedlis = []
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > (img.shape[0] * img.shape[1] * 1 / 12):  # IMPORTANT:add square condition
            cv.drawContours(image, cnt, -1, (255, 100, 100), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, False)  # getting the boounding box
            x, y, w, h = cv.boundingRect(approx)
            croppedlis.append(image[y:y + h, x:x + w])
            print(2)

        #print(area)
    #cv.imshow("shs", image)
    for i in range(len(croppedlis)):
        name="page_"+str(page)+"image"+str(i+1)+r".png"
        cv.imwrite(name, croppedlis[i])
        print(1)
        #cv.imshow(str(i), croppedlis[i])

os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Saves")
