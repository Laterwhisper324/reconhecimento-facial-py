import cv2
import camera
import numpy as np

img = cv2.imread("mesa.jpg", 0)
template = cv2.imread("cadeira2.png", 0)

img2 = img.copy()

h,w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img = img2.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

bottom_right = (location[0] + w, location[1] + h)

cv2.rectangle(img2, location, bottom_right, [0, 255, 255], 1)

cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()