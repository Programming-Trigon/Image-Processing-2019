from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Filters
import cv2
import HatchFinder


def solidity_filter(contour_list, solidity):
    output = []
    for contour in contour_list:
        area = cv2.contourArea(contour)
        hull = cv2.convexHull(contour)
        solid = 100 * area / cv2.contourArea(hull)
        if (solid < solidity[0] or solid > solidity[1]):
            continue
        output.append(contour)
    return output


CAMERA_PORT = 0

some_color = Color.Color(low=[21, 131, 124], high=[27, 255, 255])

v = Vision.Vision(camera_port=1, color=some_color,
                  filters=[Filters.area_filter], parameters=[[200]])

conts, img = v.apply_sample(camera_port=1)
print('found {} contours'.format(len(conts)))
v.display_contours(img)
cv2.waitKey()
