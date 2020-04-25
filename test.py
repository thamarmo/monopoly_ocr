import pytesseract
from PIL import Image
import cv2
import numpy as np


file_path= "resources/03.jpg"
im = Image.open(file_path)
im.save("ocr.jpg", dpi=(300, 300))
 
 
#make image b&w
im = Image.open("ocr.jpg").convert("L")
im.save("ocr.jpg")

image = cv2.imread("ocr.jpg")

#invert colour chanels
invert = cv2.bitwise_not(image)

#Crop image to name boxes
#Crop dimensions for names
crop1 = invert[428:478,683:970]
crop2 = invert[655:690,683:970]
crop3 = invert[869:918,683:970]
crop4 = invert[1086:1136,683:970]


#Global Crop width for wealth except first value
#ww1 = 2085
ww1 = 2085
ww2 = 2225
#Global variables for threshold
tn = 25
tw = 28

#Crop image to number boxes
#Crop dimensions for Total Wealth
crop1a = invert[360:430,2065:ww2]
crop2a = invert[570:655,ww1:ww2]
crop3a = invert[790:870,ww1:ww2]
crop4a = invert[1010:1100,ww1:ww2]


#Threshhold for names
retval, threshold1 = cv2.threshold(crop1,tn,255,cv2.THRESH_BINARY)
retval, threshold2 = cv2.threshold(crop2,tn,255,cv2.THRESH_BINARY)
retval, threshold3 = cv2.threshold(crop3,tn,255,cv2.THRESH_BINARY)
retval, threshold4 = cv2.threshold(crop4,tn,255,cv2.THRESH_BINARY)

#Threshhold for Total wealth
retval, threshold1a = cv2.threshold(crop1a,tw,255,cv2.THRESH_BINARY)
retval, threshold2a = cv2.threshold(crop2a,tw,255,cv2.THRESH_BINARY)
retval, threshold3a = cv2.threshold(crop3a,tw,255,cv2.THRESH_BINARY)
retval, threshold4a = cv2.threshold(crop4a,tw,255,cv2.THRESH_BINARY)

cv2.imwrite("w1.jpg",threshold1a)
cv2.imwrite("w2.jpg",threshold2a)
cv2.imwrite("w3.jpg",threshold3a)
cv2.imwrite("w4.jpg",threshold4a)

name1 = pytesseract.image_to_string(threshold1)
name2 = pytesseract.image_to_string(threshold2)
name3 = pytesseract.image_to_string(threshold3)
name4 = pytesseract.image_to_string(threshold4)

custom_config = r'--oem 3 --psm 6 outputbase digits'
wealth1 = pytesaseract.image_to_string(threshold1a, config=custom_config)
wealth2 = pytesseract.image_to_string(threshold2a, config=custom_config)
wealth3 = pytesseract.image_to_string(threshold3a, config=custom_config)
wealth4 = pytesseract.image_to_string(threshold4a, config=custom_config)
wealth1 = int(wealth1)
wealth2 = -abs(int(wealth2))
wealth3 = -abs(int(wealth3))
wealth4 = -abs(int(wealth4))
 

print(name1,name2,name3,name4)
print(wealth1,wealth2,wealth3,wealth4)
#with open("Output.csv", "w",5 ,"utf-8") as text_file:
    #text_file.write(name1+","+wealth1+"\n"+name2+","+wealth2+"\n"+name3+","+wealth3+"\n"+name4+","+wealth4)
