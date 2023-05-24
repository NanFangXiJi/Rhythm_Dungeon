import sys
import pygame

import Player
import basic_func
import Global_Variable
import Maps
import Round_Controller as RC


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

    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_ToMAP):
        basic_func.new_layer(list(), list())

    # 获取玩家的初始位置
    player_loc = list(the_map.player_init_loc)

    # 初始化玩家
    the_player = Player.Player(player_loc)

    #     处理层 1     #
    # 初始化地图层的下属Surface列表
    Global_Variable.MAIN_ATTACH[1] = [basic_func.get_empty_surface(the_map.map_dest) for i in range(6)]
    Global_Variable.MAIN_ATTACH_LOC[1] = [(0, 0) for i in range(6)]

    # 加载初始方格
    for i in range(the_map.map_size[0]):
        for j in range(the_map.map_size[1]):
            the_sq = the_map.map_Square[i][j]
            if the_sq.get_graphic() is not None:
                Global_Variable.MAIN_ATTACH[1][the_sq.obj_on.layer_for_obj].blit(the_sq.get_graphic(),
                                                                                 the_sq.square_rect)

    #     处理层 4     #
    # 加载遮罩
    sight_shadow = pygame.image.load("img/pictures/sight_shadow.png")
    sight_shadow = pygame.transform.scale(sight_shadow, Global_Variable.WINDOW_SIZE)
    Global_Variable.MAIN_ATTACH[4].append(sight_shadow)
    Global_Variable.MAIN_ATTACH_LOC[4].append((0, 0))

    basic_func.gene_all_and_draw(MainScreen)

    # 播放背景音乐
    mus = pygame.mixer.Sound(the_map.map_music_load)
    Global_Variable.music_channel[0].play(mus)

    # 初始化计时器
    map_clock = pygame.time.Clock()

    # 初始化轮控制器
    """
    轮控制器数据：
        0：轮次
        1：game_time游戏总时间
        2：on_beat是否在拍子上
        3.end_of_map是否结束
    """
    ToMap_RC = RC.Round_Controller(0, 0, False, False)


    while True:
        # RC轮初始操作
        ToMap_RC.round_init()

        # 时间操作
        map_clock.tick()
        round_time = map_clock.get_time()
        ToMap_RC.outside_data_list[1] += round_time

        # 判断是否在拍子上
        ToMap_RC.outside_data_list[2] = the_map.is_on_beat(ToMap_RC.outside_data_list[1] + the_map.map_music_fin)

        # 按键操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not ToMap_RC.outside_data_list[3] and ToMap_RC.outside_data_list[2]:
                if event.key == pygame.K_DOWN:
                    if basic_func.is_it_accessible(the_map, the_player, 1):
                        the_player.move_down()
                    else:
                        the_player.turn_down()
                elif event.key == pygame.K_UP:
                    if basic_func.is_it_accessible(the_map, the_player, 0):
                        the_player.move_up()
                    else:
                        the_player.turn_up()
                elif event.key == pygame.K_LEFT:
                    if basic_func.is_it_accessible(the_map, the_player, 2):
                        the_player.move_left()
                    else:
                        the_player.turn_left()
                elif event.key == pygame.K_RIGHT:
                    if basic_func.is_it_accessible(the_map, the_player, 3):
                        the_player.move_right()
                    else:
                        the_player.turn_right()

        # 加载方格并绘制玩家和怪物
        for i in range(len(Global_Variable.MAIN_ATTACH[1])):
            Global_Variable.MAIN_ATTACH[1][i].fill((0, 0, 0, 0))
        for i in range(the_map.map_size[0]):
            for j in range(the_map.map_size[1]):
                the_sq = the_map.map_Square[i][j]
                if the_sq.get_graphic() is not None:
                    Global_Variable.MAIN_ATTACH[1][the_sq.obj_on.layer_for_obj].blit(the_sq.get_graphic(),
                                                                                     the_sq.square_rect)
            if i == the_player.loc[0]:
                the_player.flush_status(the_player.direction, the_player.status)
                Global_Variable.MAIN_ATTACH[1][2].blit(the_player.img_list[the_player.direction][the_player.status],
                                                       the_player.creature_rect)

        # 生成并绘制
        rect_of_map = Global_Variable.MAIN_SURFACE[1].get_rect()
        rect_of_map.left = Global_Variable.WINDOW_SIZE[0] / 2 - the_player.creature_rect.left
        rect_of_map.top = Global_Variable.WINDOW_SIZE[1] / 2 - the_player.creature_rect.top
        basic_func.gene_all_and_draw(MainScreen, rect_of_map)

        # 更新RC
        ToMap_RC.update_data()
