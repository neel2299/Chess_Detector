import cv2 as cv
import imutils



image=cv.imread("Docu.jpeg")
image=imutils.resize(image,height=400,width=400)
img=cv.Canny(image,2,10,)
cv.imshow("sh",img)
croppedlis=[]
contours, hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > (img.shape[0] * img.shape[1] * 2 / 10):   #IMPORTANT:add square condition
        cv.drawContours(image, cnt, -1, (255, 100, 100), 3)
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02 * peri, False)   #getting the boounding box
        x,y,w,h = cv.boundingRect(approx)
        croppedlis.append(image[y:y+h, x:x+w])

    print(area)
cv.imshow("shs",image)
for i in range(len(croppedlis)):
    cv.imshow(str(i),croppedlis[i])
cv.waitKey(0)