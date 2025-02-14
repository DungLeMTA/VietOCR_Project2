# # -*- coding: utf-8 -*-
# # License: Anti-996, Anti-995, Follow-955 (ignore if the license is not exist)
# # miniconda is recommanded
# # conda install pillow numpy opencv -c conda-forge -y
# from __future__ import print_function
#
# import cv2
# from PIL import Image
# import io
# import numpy as np
# try:
#     import urllib.request as urllib
# except ModuleNotFoundError:
#     import urllib
#
# # read an image by filepath or image_url, im=filepath/image_url
# def imgread(im):
#     # try:
#     #     image = Image.open(io.BytesIO(urllib.urlopen(im).read()))
#     # except ValueError:
#     #     try:
#     #         image = Image.open(im)
#     #     except FileExistsError:
#     #         return None
#     try:
#         image = cv2.cvtColor(cv2.imread(im), cv2.COLOR_RGB2BGR)
#     except:
#         return None
#     return image
#
# # your image filepath or url
# img = "B:\PycharmProjects\VietOCR_Project\\test\\vanban2.png"
#
# im = imgread(img)
# image = im.copy()
#
# # cv2.imshow('image', im)
# # cv2.waitKey(0)
#
# im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
# cv2.imshow("gray image", im)
# cv2.waitKey(0)
#
# dst = cv2.adaptiveThreshold(~im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -2)
#
# # cv2.imshow("binary image", dst)
# # cv2.waitKey(0)
#
# # copy dst, then for horizontal and vertical lines' detection.
# horizontal = dst.copy()
# vertical = dst.copy()
# scale = 15  # play with this variable in order to increase/decrease the amount of lines to be detected
#
# # Specify size on horizontal axis
# print(horizontal.shape)
# horizontalsize = horizontal.shape[1] // scale
# horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
# horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
# horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))
# cv2.imshow("horizontal line", horizontal)
# cv2.waitKey(0)
#
# # vertical
# verticalsize = vertical.shape[0] // scale
# verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
# vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
# vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))
# cv2.imshow("verticalsize line", vertical)
# cv2.waitKey(0)
#
# # table line
# table = horizontal + vertical
# cv2.imshow("table", table)
# cv2.waitKey(0)
#
# # the joint points between horizontal line and vertical line.
# joints = cv2.bitwise_and(horizontal, vertical)
# cv2.imshow("joint points", joints)
# cv2.waitKey(0)
# # image = cv2.imread('img_2.png')
# pointss = []
# for i in range(im.shape[0]):
#     points = []
#     for j in range(im.shape[1]):
#
#         if joints[i][j] == 255:
#             point = []
#             point.append(j)
#             point.append(i)
#             #print( str(i) + " " + str(j))
#             points.append(point)
#     if len(points) > 0:
#         pointss.append(points)
# #print(pointss)
#
# bourders = []
# for i in range(len(pointss) - 1 ):
#     #print(pointss[i])
#     if len(pointss[i]) == len(pointss[i+1]):
#
#         for j in range(len(pointss[i]) -1):
#             bourder = []
#             bourder.append(pointss[i][j])
#             bourder.append(pointss[i+1][j+1])
#             print(bourder)
#             bourders.append(bourder)
#
# red = (0,0,255)
# for point in bourders:
#     cv2.rectangle(image,  tuple(point[0]),tuple(point[1]), red, 1)
#
# cv2.imshow('anh', image)
# cv2.waitKey(0)



# -*- coding: utf-8 -*-
# License: Anti-996, Anti-995, Follow-955 (ignore if the license is not exist)
# miniconda is recommanded
# conda install pillow numpy opencv -c conda-forge -y
from __future__ import print_function

import cv2
from PIL import Image
import io
import numpy as np
try:
    import urllib.request as urllib
except ModuleNotFoundError:
    import urllib

# read an image by filepath or image_url, im=filepath/image_url
def imgread(im):
    # try:
    #     image = Image.open(io.BytesIO(urllib.urlopen(im).read()))
    # except ValueError:
    #     try:
    #         image = Image.open(im)
    #     except FileExistsError:
    #         return None
    try:
        image = cv2.cvtColor(cv2.imread(im), cv2.COLOR_RGB2BGR)
    except:
        return None
    return image

# your image filepath or url
img = "B:\PycharmProjects\VietOCR_Project\img_2.png"

im = imgread(img)

# cv2.imshow('image', im)
# cv2.waitKey(0)

im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
#cv2.imshow("gray image", im)
#cv2.waitKey(0)

dst = cv2.adaptiveThreshold(~im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -2)

# cv2.imshow("binary image", dst)
# cv2.waitKey(0)

# copy dst, then for horizontal and vertical lines' detection.
horizontal = dst.copy()
vertical = dst.copy()
scale = 15  # play with this variable in order to increase/decrease the amount of lines to be detected

# Specify size on horizontal axis
print(horizontal.shape)
horizontalsize = horizontal.shape[1] // scale
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))
#cv2.imshow("horizontal line", horizontal)
#cv2.waitKey(0)

# vertical
verticalsize = vertical.shape[0] // scale
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))
#cv2.imshow("verticalsize line", vertical)
#cv2.waitKey(0)

# table line
table = horizontal + vertical
#cv2.imshow("table", table)
#cv2.waitKey(0)

# the joint points between horizontal line and vertical line.
joints = cv2.bitwise_and(horizontal, vertical)
#cv2.imshow("joint points", joints)
#cv2.waitKey(0)
image = cv2.imread(img)
pointss = []
for i in range(im.shape[0]):
    points = []
    for j in range(im.shape[1]):

        if joints[i][j] == 255:
            point = []
            point.append(j)
            point.append(i)
            #print( str(i) + " " + str(j))
            points.append(point)
    if len(points) > 0:
        pointss.append(points)
print(pointss)

#cắt ảnh
print(pointss[0][0][0])
print(pointss[0][0][0])
for i in range(len(pointss) - 1):
    for j in range(i+1, len(pointss)):
        if pointss[i][-1][0] == pointss[j][-1][0]:
            crop = im[pointss[i][0][1]: pointss[j][0][1], 0: im.shape[0]]
            for ii in range(len(pointss[i]) - 1):
                for iii in range(ii+1, len(pointss[i])):
                    crop_1 = crop[:, pointss[i][ii][0]:pointss[i][iii][0]]
                    try:
                        cv2.imshow('img' + str(j) + "_" + str(ii), crop_1)
                        cv2.imwrite('./crop_table/img' + str(j) + '_' + str(ii)+'.png',crop_1)
                    except:
                        pass
                    break
            break

bourders = []
for i in range(len(pointss) - 1 ):
    #print(pointss[i])
    if len(pointss[i]) == len(pointss[i+1]):

        for j in range(len(pointss[i]) -1):
            bourder = []
            bourder.append(pointss[i][j])
            bourder.append(pointss[i+1][j+1])
            #print(bourder)
            bourders.append(bourder)

red = (0,0,255)
for point in bourders:
    cv2.rectangle(image,  tuple(point[0]),tuple(point[1]), red, 1)

cv2.imshow('anh', image)
cv2.waitKey(0)


