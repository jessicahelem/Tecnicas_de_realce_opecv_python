#encoding-utf8
import cv2
import numpy as np

img = cv2.imread('foto.jpg',1)
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# IMAGEM NEGATIVA

img_not = cv2.bitwise_not(imgGray)
res1 = np.hstack((imgGray,img_not)) #stacking images side-by-side

cv2.imwrite('resultados/negativa.jpg',img_not)



# NORMALIZAÇÃO DA IMAGEM

equ = cv2.equalizeHist(imgGray)
res2 = np.hstack((imgGray,equ)) #stacking images side-by-side
cv2.imwrite('resultados/normalizacao.jpg',res2)

cv2.imshow("Negativa",res1)
cv2.imshow("Normalização",res2)

cv2.waitKey(0)
cv2.destroyAllWindows()