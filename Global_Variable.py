"""
用于存储全局变量的文件
"""
import pygame

#     常量区     #

# 游戏标题
GAME_TITLE = 'Rhythm Dungeon'

# 窗口大小
WINDOW_SIZE = (1280, 960)

# 常用颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 每个阶段的图层数
LAYER_START_PROCESS = 3
LAYER_MENU = 3

#     变量区     #

# 全局图像层数组
MAIN_ATTACH = list()

# 全局图像层对应位置数组
MAIN_ATTACH_LOC = list()

# 全局实际图层Surface
MAIN_SURFACE = list()
