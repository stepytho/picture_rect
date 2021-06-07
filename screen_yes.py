import cv2
import time,PIL,os
from PIL import ImageGrab
import numpy as np

#截图
def cut():
    global img
    scrren_cut()
    img = cv2.imread('screen.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    os.remove('screen.jpg')

def get_image_rotation(image):
    #通用写法，即使传入的是三通道图片依然不会出错
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation = 90

    #得到旋转矩阵，第一个参数为旋转中心，第二个参数为旋转角度，第三个参数为旋转之前原图像缩放比例
    M = cv2.getRotationMatrix2D(center, -rotation, 1)
    #进行仿射变换，第一个参数图像，第二个参数是旋转矩阵，第三个参数是变换之后的图像大小
    image_rotation = cv2.warpAffine(image, M, (width,height))
    return image_rotation

#顺时针旋转90度
def RotateClockWise90(img):
    trans_img = cv2.transpose(img)
    new_img = cv2.flip(trans_img, 1)
    return new_img

#逆时针旋转90度
def RotateAntiClockWise90(img):
    trans_img = cv2.transpose(img)
    new_img = cv2.flip(trans_img, 0)
    return new_img

#展示旋转后的图片
def show_pic(path):
    img = cv2.imread(path)
    cv2.imshow("show_pic", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scrren_cut():
    beg = time.time()
    debug = False
    # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    image = ImageGrab.grab()
    image.save("screen.jpg")
    # PIL image to OpenCV image
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5) 
        cv2.imshow('image', img2)
        min_x = min(point1[0],point2[0])     
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]

        cv2.imwrite('test.png', cut_img)
        cut_img2 = RotateClockWise90(cut_img)
        cv2.imwrite('test_angle.png', cut_img2)
        cut_img3 = RotateAntiClockWise90(cut_img)
        cv2.imwrite('test_anti_angle.png', cut_img3)
        

if __name__ == "__main__":
  cut()
  path = "test.png"
  show_pic(path)

