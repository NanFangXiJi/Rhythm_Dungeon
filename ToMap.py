import sys
import pygame

import basic_func
import Global_Variable
import Maps


def ToMap(MainScreen: pygame.Surface, map_index: int = Global_Variable.NEXT_MAP):
    """
    此处处理进入地图的阶段
    ToMap阶段的层：
        0：底部预置层
        1：地图层
            1.0：地板层
            1.1：地上物层
            1.2：直立物层
            1.3：地图文字层
            1.4：地图效果层
        2：效果层
        3：文字层
        4：遮罩层
        5：顶部预置层
    :param MainScreen: 主窗口
    :param map_index: 进入的地图编号
    """
    #     初始化阶段     #

    # 根据地图编号初始化地图对象
    the_map = Maps.maps(map_index)

    # 读取地图
    pass

    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_ToMAP):
        basic_func.new_layer(list(), list())

    # 初始化地图层的下属Surface列表
    Global_Variable.MAIN_ATTACH[1] = [basic_func.get_empty_surface(the_map.map_dest) for i in range(6)]
    Global_Variable.MAIN_ATTACH_LOC[1] = [(0, 0) for i in range(6)]  # 这行仅供测试用

    # 加载初始方格
    for i in range(the_map.map_size[0]):
        for j in range(the_map.map_size[1]):
            the_sq = the_map.map_Square[i][j]
            Global_Variable.MAIN_ATTACH[1][the_sq.obj_on.layer_for_obj].blit(the_sq.get_graphic(), the_sq.square_rect)

    # 生成并绘制
    basic_func.gene_all_and_draw_for_map(MainScreen)

    while True:
        # 按键操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
