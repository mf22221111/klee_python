import time
import win32gui, win32ui, win32con, win32api
from pymouse import PyMouse
import numpy as np
import matplotlib.pyplot as plt
# from ctypes import *
import os
from pylab import *
from PIL import Image

def window_capture(filename):
  hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 获取监控器信息
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  # w = MoniterDev[0][2][2]
  # h = MoniterDev[0][2][3]
  w=620
  h=1080
  #print w,h　　　#图片大小
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)
  # 截取从左上角（0，0）长宽为（w，h）的图片
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(mfcDC, filename)

  img = Image.open("haha.jpg")
  img_1 = img.convert('L')  # 转灰度
  img_2 = array(img_1,'f') #转白色

  m = PyMouse()
  a = m.position()  # 获取当前坐标的位置
  # print(img_2[780][80]+img_2[780][70]+img_2[780][90])
  hhh=720
  if img_2[hhh][80]+img_2[hhh][70]+img_2[hhh][90]<3*200:
    m.click(80, 900)  # 移动并且在(x,y)位置左击
  if img_2[hhh][240]+img_2[hhh][230]+img_2[hhh][250]<3*200:
    m.click(240, 900)  # 移动并且在(x,y)位置左击
  if img_2[hhh][400]+img_2[hhh][410]+img_2[hhh][390]<3*200:
    m.click(400, 900)  # 移动并且在(x,y)位置左击
  if img_2[hhh][560]+img_2[hhh][570]+img_2[hhh][550]<3*200:
    m.click(560, 900)  # 移动并且在(x,y)位置左击
  # # print('色块： ',aaa)
  img_1.save('h灰度.jpg')
  img.close()

used_time=0;
arrey_time=0.1
for i in range(10):
  beg = time.time()
  window_capture("haha.jpg")
  end = time.time()

  used_time=end - beg
  print('延时',used_time,'     ',i)
  if used_time<arrey_time:
    time.sleep(arrey_time+beg-end)