# paint_init.py

from FilePathList import ASSET_DIR
from PIL import Image, ImageDraw, ImageFont
import ctypes
from os import getcwd

# 获取屏幕大小
user32 = ctypes.windll.user32
WIN_WIDTH = user32.GetSystemMetrics(0) * 2
WIN_HEIGHT = user32.GetSystemMetrics(1) * 2

# 设置颜色
BACKGROUND_COLOR = '#363636'
TITLE_COLOR = '#f0f0f0'
NORMAL_COLOR = '#e0e0e0'
PROJECT_COLOR = '#9b1b1b'
TIME_COLOR = '#40afe3'

# 设置字体
font_path = ASSET_DIR + r'Font\杨任东竹石体.ttf'
title_size = int(WIN_HEIGHT / 16)
TITLE_FONT = ImageFont.truetype(font_path, title_size, encoding='UTF-8')

normal_size = int(WIN_HEIGHT / 27)
NORMAL_FONT = ImageFont.truetype(font_path, normal_size, encoding='UTF-8')

small_size = int(WIN_HEIGHT / 32)
SMALL_FONT = ImageFont.truetype(font_path, small_size, encoding='UTF-8')

# 初始化画布
WALLPAPER = Image.new('RGB', (2560, 1600), BACKGROUND_COLOR)
DRAW = ImageDraw.Draw(WALLPAPER)
WALLPAPER_PATH = ASSET_DIR + r'Wallpaper\active.png'