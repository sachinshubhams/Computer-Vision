import cv2 as cv

fix_img=cv.imread('Computer-Vision-with-Python/DATA/00-puppy.jpg')
while True:
    cv.imshow('Puppy',fix_img)
    #if we waited at least 1 ms AND we have pressed the Esc key
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()