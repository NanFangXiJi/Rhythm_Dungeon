"""
控制全局常用的函数
"""

import sys
import pygame

import Global_Variable


#     基础操作部分     #

# 初始化全部图层
def init_global_generation():
    """
    每个阶段结束后初始化全部图层，以便在下一个阶段从零开始生成
    """
    Global_Variable.MAIN_ATTACH = list()
    Global_Variable.MAIN_ATTACH_LOC = list()
    Global_Variable.MAIN_SURFACE = list()

def gene_all_and_draw(MainScreen: pygame.Surface):
    """
    确定所有的图层均可用，并需要立即刷新屏幕以绘制，则使用该函数
    生成所有图层并绘制的函数
    :param MainScreen: 主窗口
    """
    generate('ALL')
    draw(MainScreen)

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
def generate(layer_index: int = 'ALL'):
    """
    将已经加载好的层生成至全局变量MAIN_SURFACE列表待用
    可以输入层数选择需要生成的层，也可以选择生成所有层
    :param layer_index: 要重生成的图层序号(从0开始数)，默认值ALL表示全部重新生成
    """
    if layer_index == 'ALL':
        # 清空生成列表
        Global_Variable.MAIN_SURFACE.clear()

        # 逐层、逐个生成
        for i in range(len(Global_Variable.MAIN_ATTACH)):
            # 初始化生成层：全透明
            new_surface = pygame.Surface(Global_Variable.WINDOW_SIZE, pygame.SRCALPHA)
            new_surface.fill((0, 0, 0, 0))
            for j in range(len(Global_Variable.MAIN_ATTACH[i])):
                # 在生成层上生成
                new_surface.blit(Global_Variable.MAIN_ATTACH[i][j],
                                 Global_Variable.MAIN_ATTACH_LOC[i][j])
            # 将生成结束的层加入生成列表
            Global_Variable.MAIN_SURFACE.append(new_surface)

    else:
        # 初始化生成层
        new_surface = pygame.Surface(Global_Variable.WINDOW_SIZE)
        for j in range(len(Global_Variable.MAIN_ATTACH[layer_index])):
            # 在生成层上生成
            new_surface.blit(Global_Variable.MAIN_ATTACH[layer_index][j],
                             Global_Variable.MAIN_ATTACH_LOC[layer_index][j])
        # 将生成结束的层替代原有层加入生成列表
        Global_Variable.MAIN_SURFACE[layer_index] = new_surface


#     画面绘制部分     #

# 屏幕刷新绘制图像
def draw(MainScreen: pygame.Surface):
    """
    先重置主画面，然后将存储已经生成好的层的全局变量MAIN_SURFACE逐层绘制到主画面上，并且刷新屏幕
    :param MainScreen: 主窗口
    """
    # 重置主画面
    MainScreen.fill(Global_Variable.BLACK)
    # 将最终图像生成至主画面上
    for i in range(len(Global_Variable.MAIN_SURFACE)):
        MainScreen.blit(Global_Variable.MAIN_SURFACE[i], (0, 0))
    # 刷新画面
    pygame.display.flip()
