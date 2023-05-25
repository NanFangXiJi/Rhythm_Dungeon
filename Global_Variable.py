"""
用于存储全局变量的文件
"""
import pygame

import Monster
import OBJ

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
LAYER_ToMAP = 6
LAYER_GAME_OVER = 3

# 游戏地图总数
MAP_NUM = 1

# obj_rule文件路径
load_of_obj_rule = "data/obj_rule.xlsx"

# obj的定义列表
obj_rule_list = list()

# 储存全体obj的列表
obj_list: list[OBJ.obj] = list()

# monster_rule文件路径
load_of_monster_rule = "data/monster_rule.xlsx"

# monster的定义列表
monster_rule_list = list()

# 储存全体monster的列表
monster_list: list[Monster.Monster] = list()

# 音频通道个数
CHANNEL = 2

# 全局音频通道
music_channel: list[pygame.Channel] = list()

# 玩家初始攻击力
init_attack_of_player = 1

# 玩家初始最大血量
init_max_blood_of_player = 4


#     变量区     #

# 全局图像层数组
MAIN_ATTACH = list()

# 全局图像层对应位置数组
MAIN_ATTACH_LOC = list()

# 全局实际图层Surface
MAIN_SURFACE = list()

# 下一个界面
NEXT_PAGE = int()

# 下一个地图
NEXT_MAP = int()
