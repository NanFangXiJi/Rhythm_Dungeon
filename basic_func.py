"""
控制全局常用的函数
"""

import sys
from typing import Union
import pandas
import pygame

import Global_Variable
import OBJ
import Monster
import Maps
import Creature


#     基础操作部分     #

# 初始化mon_list
def init_mon_list():
    """
    初始化mon_list，加载所有的mon并储存在mon_list中
    """
    for i in range(len(Global_Variable.monster_rule_list)):
        Global_Variable.monster_list.append(Monster.Monster(i))


# 初始化obj_list
def init_obj_list():
    """
    初始化obj_list，加载所有的obj并储存在obj_list中
    """
    for i in range(len(Global_Variable.obj_rule_list)):
        Global_Variable.obj_list.append(OBJ.obj(i))


# 初始化全部图层
def init_global_generation():
    """
    每个阶段结束后初始化全部图层，以便在下一个阶段从零开始生成
    """
    Global_Variable.MAIN_ATTACH = list()
    Global_Variable.MAIN_ATTACH_LOC = list()
    Global_Variable.MAIN_SURFACE = list()


# 全部生成并绘制
def gene_all_and_draw(MainScreen: pygame.Surface, dest: tuple[int, int] = (0, 0)):
    """
    确定所有的图层均可用，并需要立即刷新屏幕以绘制，则使用该函数
    生成所有图层并绘制的函数
    :param MainScreen: 主窗口
    :param dest: 位置，其实是给to_map留的后门，方便改换位置
    """
    generate('ALL')
    draw(MainScreen, dest)


def gene_all_and_draw_for_map(MainScreen: pygame.Surface):
    """
    为Map放大而特殊创造的函数
    :param MainScreen: 主窗口
    """
    generate('ALL')
    rect = Global_Variable.MAIN_SURFACE[1].get_rect()
    Global_Variable.MAIN_SURFACE[1] = pygame.transform.scale(Global_Variable.MAIN_SURFACE[1],
                                                             (rect.width * 2, rect.height * 2))
    draw(MainScreen)


def get_empty_surface(dest: tuple[int, int]):
    new_surface = pygame.Surface(dest, pygame.SRCALPHA)
    new_surface.fill((0, 0, 0, 0))
    return new_surface


#     运算部分     #

# 判断行动是否能够进行
def is_it_accessible(the_map: Maps.maps, creature: Creature.Creature, direction: int):
    """
    判断能不能进行行动
    :param the_map: 地图本身
    :param creature: 行动生物
    :param direction: 行动方向
    :return: bool量
    """
    cre_loc = creature.loc
    if direction == 0:
        return the_map.map_Square[cre_loc[0] - 1][cre_loc[1]].obj_on.accessible == 1
    elif direction == 1:
        return the_map.map_Square[cre_loc[0] + 1][cre_loc[1]].obj_on.accessible == 1
    elif direction == 2:
        return the_map.map_Square[cre_loc[0]][cre_loc[1] - 1].obj_on.accessible == 1
    elif direction == 3:
        return the_map.map_Square[cre_loc[0]][cre_loc[1] + 1].obj_on.accessible == 1


# 计算闪烁透明度
def calculate_alpha(round: int, this_round: int):
    """
    通过二次函数255-x**2/255来返回透明度值，达到闪烁的效果
    :param round: 每次完整闪烁中修改多少次透明度
    :param this_round: 这是本次完整闪烁的第几次，从0开始数
    :return: 返回下一次的透明度
    """
    alpha = 255 - (-255 + (510 / round) * this_round) ** 2 / 255
    this_round += 1
    return alpha


# 获取物品绘制方法
def obj_graphics_calculate(graphics_msg: str):
    """
    这是将从文件中读取的物体绘制方法转换为列表的方法
    文件中的写法如下：
        pic1,pic2,|,pic1,pic3,pic4,|,pic6,pic7
    符号|用来分隔物品每一个状态的图片
    符号,用来分隔所有意义上“不同的东西”
    上面的最终会被转化为列表如下：
        [['pic1','pic2'],['pic1','pic3','pic4'],['pic6','pic7']]
    :param graphics_msg: 读取的绘制方法
    :return: 绘制方法列表
    """
    graphics_msg_list = graphics_msg.split(',')
    graphics_list = []
    temp_list = []
    for msg in graphics_msg_list:
        if msg == '|':
            graphics_list.append(temp_list.copy())
            temp_list = []
        else:
            temp_list.append(msg)
    if len(temp_list) > 0:
        graphics_list.append(temp_list)
    del temp_list
    return graphics_list


#     画面加载部分     #

# 将surface变为标准大小
def sur_to_standard_square_size(sur: pygame.Surface):
    """
    将读取文件后绘制的surface变为标准方格大小50x50，直接作用在surface上
    似乎并不起作用，因此禁用，建议是直接获得正确大小的surface
    :param sur: 需要改变的surface
    """
    size = sur.get_size()
    if size != (50, 50):
        pygame.transform.scale(sur, (50, 50))


#     画面生成部分     #

# 顶部新建图像层
def new_layer(layer: list[pygame.Surface] = list(), layer_loc: list[pygame.Rect] = list()):
    """
    加载阶段，在顶层新建一层
    既可传入已经加载结束的层，也可以传入空层以后再加载
    不写实参则默认为传入空层
    :param layer: 需要新建到顶部的层
    :param layer_loc: 图层对应的位置列表
    """
    Global_Variable.MAIN_ATTACH.append(layer)
    Global_Variable.MAIN_ATTACH_LOC.append(layer_loc)


# 生成对应图层
def generate(layer_index: Union[int, str] = 'ALL'):
    """
    将已经加载好的层生成至全局变量MAIN_SURFACE列表待用
    可以输入层数选择需要生成的层，也可以选择生成所有层
    :param layer_index: 要重生成的图层序号(从0开始数)，默认值ALL表示全部重新生成
    """
    if layer_index == 'ALL':
        # 清空生成列表
        Global_Variable.MAIN_SURFACE.clear()

        # 逐层、逐个生成
        if len(Global_Variable.MAIN_ATTACH) > 0:
            for i in range(len(Global_Variable.MAIN_ATTACH)):
                # 初始化生成层：全透明
                new_surface = pygame.Surface(Global_Variable.WINDOW_SIZE, pygame.SRCALPHA)
                new_surface.fill((0, 0, 0, 0))
                if len(Global_Variable.MAIN_ATTACH[i]) > 0:
                    for j in range(len(Global_Variable.MAIN_ATTACH[i])):
                        # 在生成层上生成
                        new_surface.blit(Global_Variable.MAIN_ATTACH[i][j],
                                         Global_Variable.MAIN_ATTACH_LOC[i][j])
                # 将生成结束的层加入生成列表
                Global_Variable.MAIN_SURFACE.append(new_surface)
    else:
        # 初始化生成层
        new_surface = pygame.Surface(Global_Variable.WINDOW_SIZE, pygame.SRCALPHA)
        new_surface.fill((0, 0, 0, 0))
        if len(Global_Variable.MAIN_ATTACH[layer_index]) > 0:
            for j in range(len(Global_Variable.MAIN_ATTACH[layer_index])):
                # 在生成层上生成
                new_surface.blit(Global_Variable.MAIN_ATTACH[layer_index][j],
                                 Global_Variable.MAIN_ATTACH_LOC[layer_index][j])
        # 将生成结束的层替代原有层加入生成列表
        Global_Variable.MAIN_SURFACE[layer_index] = new_surface


def generate_for_map(layer_index: int):
    generate(layer_index)
    if layer_index == 1:
        rect = Global_Variable.MAIN_SURFACE[1].get_rect()
        Global_Variable.MAIN_SURFACE[1] = pygame.transform.scale(Global_Variable.MAIN_SURFACE[1],
                                                                 (rect.width * 2, rect.height * 2))


#     画面绘制部分     #

# 屏幕刷新绘制图像
def draw(MainScreen: pygame.Surface, dest: tuple[int, int] = (0, 0)):
    """
    先重置主画面，然后将存储已经生成好的层的全局变量MAIN_SURFACE逐层绘制到主画面上，并且刷新屏幕
    :param MainScreen: 主窗口
    :param dest: 位置，其实是给to_map留的后门，方便改换位置
    """
    # 重置主画面
    MainScreen.fill(Global_Variable.BLACK)
    # 将最终图像生成至主画面上
    for i in range(len(Global_Variable.MAIN_SURFACE)):
        if i == 1:
            MainScreen.blit(Global_Variable.MAIN_SURFACE[i], dest)
        else:
            MainScreen.blit(Global_Variable.MAIN_SURFACE[i], (0, 0))
    # 刷新画面
    pygame.display.flip()


#     文件处理 读     #
def read_obj_rule():
    """
    实现初始化物体列表的读取，在最开始处进行
    """
    obj_rule_file = pandas.read_excel(Global_Variable.load_of_obj_rule)
    Global_Variable.obj_rule_list = obj_rule_file.values.tolist()


def read_monster_rule():
    """
    实现初始化怪物列表的读取，在最开始处进行
    """
    monster_rule_file = pandas.read_excel(Global_Variable.load_of_monster_rule)
    Global_Variable.monster_rule_list = monster_rule_file.values.tolist()
