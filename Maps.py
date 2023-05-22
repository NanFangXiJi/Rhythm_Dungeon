import pygame.mixer

import Square


class maps:
    map_index: int  # 地图编号
    map_name: str  # 地图名

    map_size: tuple[int, int]  # 一个二元元组，确定maps有几行几列
    map_dest: tuple[int, int]  # 一个二元元组，确定maps的像素大小
    map_Square: list[list[Square.Square]]  # 一个二维数组，维护地图所有的方格，位置表示为几行几列

    map_music_load: str  # 地图对应音乐的路径
    map_music_BPM: int | float  # 地图对应音乐的BPM速度

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
        # 初始化地图名、地图大小、地图方格、地图音乐路径、地图音乐对应BPM
        map_message_list = map_file_list[0].split(',')
        self.map_size = (eval(map_message_list[2]), eval(map_message_list[3]))
        self.map_dest = (50 * eval(map_message_list[2]), 50 * eval(map_message_list[3]))
        self.map_Square = list()
        # 下面这一部分需要修改成能读取初始化的方法
        for i in range(self.map_size[0]):
            self.map_Square.append(list())
            for j in range(self.map_size[1]):
                self.map_Square[i].append(Square.Square((i, j)))
        self.map_music_load = '/music/' + map_message_list[4]
        self.map_music_BPM = eval(map_message_list[5])

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
