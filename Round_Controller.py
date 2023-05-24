import pygame


class Round_Controller:
    """
    这是循环控制器类，借此实现对循环的简易操作
    """
    __inside_data_list: list  # 储存旧版循环数据，0号元素默认为循环次数，私有
    outside_data_list: list  # 储存可修改的循环数据，0号元素默认为循环次数，公共
    __init_dict_for_data_list: dict  # out_side_data_list的初始化字典

    def __init__(self):
        self.__inside_data_list = [0]
        self.outside_data_list = [0]

    def round_init(self):
        """
        每轮开始时用于初始化需要初始化的数据
        :return:
        """
        for key, val in self.__init_dict_for_data_list:
            self.outside_data_list[key] = val

    def is_it_same(self, data_index: int):
        """
        用来比较本轮数据与上轮数据是否相同的
        :param data_index: 要比较的数据的下标
        :return:bool值
        """
        if self.__inside_data_list[data_index] == self.outside_data_list[data_index]:
            return True
        else:
            return False

    def update_data(self):
        """
        在循环的最后更新旧版数据，并获得下一轮的轮次
        """
        self.__inside_data_list.clear()
        self.__inside_data_list = self.outside_data_list.copy()
        self.outside_data_list[0] += 1
