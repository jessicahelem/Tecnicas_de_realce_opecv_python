import cv2
import numpy as np


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

img = cv2.imread('foto.jpg',1)
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

res = np.hstack((imgGray,adjust_gamma(imgGray,2.0)))

cv2.imwrite('resultados/OperaçãoGamma.jpg',res)
cv2.imshow('Operação Gamma',res)

cv2.waitKey(0)
cv2.destroyAllWindows()