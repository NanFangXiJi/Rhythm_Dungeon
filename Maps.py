import pygame.mixer

import Square


class maps:
    map_index: int  # 地图编号
    map_name: str  # 地图名

    map_size: tuple[int, int]  # 一个二元元组，确定maps有几行几列
    map_dest: tuple[int, int]  # 一个二元元组，确定maps的像素大小
    map_Square: list[list[Square.Square]]  # 一个二维数组，维护地图所有的方格，位置表示为几行几列

    player_init_loc: tuple[int, int]  # 一个二元数组，确定玩家的初始位置

    map_music_load: str  # 地图对应音乐的路径
    map_music_BPM: int | float  # 地图对应音乐的BPM速度
    map_music_fin: int  # 音乐节拍补偿
    beat_long: float  # 拍子的长度

    def __init__(self, index: int):
        """

        未完成

        maps的构造函数
        :param index: 地图的编号
        """
        # 初始化地图编号
        self.map_index = index
        # 读文件
        map_file_list = self.read_map_file()
        # 初始化地图名、地图大小、地图方格、地图音乐路径、地图音乐对应BPM等
        map_message_list = map_file_list[0].split(',')
        self.map_size = (eval(map_message_list[2]), eval(map_message_list[3]))
        self.map_dest = (50 * eval(map_message_list[2]), 50 * eval(map_message_list[3]))
        self.player_init_loc = (eval(map_message_list[6]), eval(map_message_list[7]))
        self.map_Square = list()

        # 读取初始地图
        temp_list = self.prepare_map_file(map_file_list[1:])
        for i in range(self.map_size[0]):
            self.map_Square.append(list())
            for j in range(self.map_size[1]):
                uni_temp_list = temp_list[i][j].split(',')
                self.map_Square[i].append(Square.Square((i, j), eval(uni_temp_list[0]), eval(uni_temp_list[1])))
        self.map_music_load = 'music/' + map_message_list[4]
        self.map_music_BPM = eval(map_message_list[5])
        self.map_music_fin = eval(map_message_list[8])
        self.beat_long = 60 * 1000 / self.map_music_BPM

    def read_map_file(self):
        """
        读取地图文件的信息
        :return: 返回读取到的字符串
        """
        with open('maps/' + str(self.map_index) + '.txt', 'r', encoding='utf-8') as f:
            return f.readlines()

    def get_size(self):
        return self.map_size

    def get_music(self):
        """
        加载地图背景音乐的函数
        :return: 返回地图背景音
        """
        return pygame.mixer.Sound(self.map_music_load)

    def prepare_map_file(self, map_file_list: list[str]):
        new_list = [sr.split(';') for sr in map_file_list]
        return new_list

    def is_on_beat(self, timer: int):
        # 拍点的三分之一为判定区间
        pal = timer % self.beat_long
        if pal > self.beat_long * 3 / 4 or pal < self.beat_long / 4:
            return True
        else:
            return False
