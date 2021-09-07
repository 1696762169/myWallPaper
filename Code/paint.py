# paint.py

import paint_init
from Routine import r_paint
from  Event import  e_paint
import win32gui, win32con, win32api

# 生成壁纸图片
def generateWallpaper():
    r_paint.paint_routine()
    e_paint.paint_event()
    paint_init.WALLPAPER.save(paint_init.WALLPAPER_PATH)

# 将图片设置为壁纸，实现原理暂时未知
def setWallpaper():
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, 'WallpaperStyle', 0, win32con.REG_SZ, '0') # 最后一个参数：0代表不缩放，1代表等比例适应屏幕缩放，2代表适应屏幕拉伸
    win32api.RegSetValueEx(k, 'TileWallpaper', 0, win32con.REG_SZ, '0') # 最后一个参数：0代表置于左上角，1代表居中
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, paint_init.WALLPAPER_PATH, 1 + 2)

if __name__ == '__main__':
    generateWallpaper()
    setWallpaper()