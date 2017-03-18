import cv2
import numpy as np 
# We nned to import matplotlib to create our histogramm plots
from matplotlib import  pyplot as plt
import pyparsing # It's need to inport this Lib that matplotlib will works
'''    
 cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])**\n",
    
    - images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]"
    - channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. 
      For example, if input is grayscale image, its value is [0]. For color image, 
      you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
    - mask : mask image. To find histogram of full image, it is given as "None".
      But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
    - histSize : this represents our BIN count. Need to be given in square brackets.
      For full scale, we pass [256].
    - ranges : this is our RANGE. Normally, it is [0,256]."

'''

image = cv2.imread('D:\CV\MasterOpenCV\Sourse\images\/tobago.jpg')
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flatens our image array
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channel
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
	histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
	plt.plot(histogram2, color = col)
	plt.xlim([0, 256])

plt.show


'''   
Test for changes in the Git rep !!!



'''