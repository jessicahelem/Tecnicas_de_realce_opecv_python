import cv2
import math
import numpy as np


def logTransform(c, img):
    # 3 RGB
    '''h,w,d = img.shape[0],img.shape[1],img.shape[2]
    new_img = np.zeros((h,w,d))
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i,j,k] = c*(math.log(1.0+img[i,j,k]))'''

    #  Exclusive
    h, w = img.shape[0], img.shape[1]
    new_img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.log(1.0 + img[i, j]))

    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)

    return new_img


# replace as your image path
img = cv2.imread('foto.jpg')

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

log_img = np.hstack((imgGray,logTransform(2.0, imgGray)))

cv2.imwrite('resultados/TransformacaoLogaritimica.jpg', log_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
