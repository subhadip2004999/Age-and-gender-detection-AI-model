#install packages
!pip install deepface
#import library the package
from deepface import DeepFace
#now import your image
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("PASTE YOUR IMAGE PATH")
plt.imshow(img1[:,:,::-1])
plt.show()
#analyze the image as result
result=DeepFace.analyze(img1, actions=['age','gender'])
print(result[0]['age'])
print(result[0]['dominant_gender'])
