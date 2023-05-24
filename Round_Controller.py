import pygame


class Round_Controller:
    """
    这是循环控制器类，借此实现对循环的简易操作
    """
    __inside_data_list: list  # 储存旧版循环数据，0号元素默认为循环次数，私有
    outside_data_list: list  # 储存可修改的循环数据，0号元素默认为循环次数，公共
    init_dict_for_data_list: dict  # out_side_data_list的初始化字典

    def __init__(self, *args):
        if len(args) == 0:
            self.__inside_data_list = [0]
            self.outside_data_list = [0]
        else:
            self.__inside_data_list = list()
            self.outside_data_list = list()
            for ele in args:
                self.__inside_data_list.append(ele)
                self.outside_data_list.append(ele)
        self.init_dict_for_data_list = dict()

    def round_init(self):
        """
        每轮开始时用于初始化需要初始化的数据
        """
        if len(self.init_dict_for_data_list) > 0:
            for key, val in self.init_dict_for_data_list.items():
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

    def compare_with_last(self, data_index: int):
        """
        用来比较本轮数据与上轮数据，只能处理数字等可以比较的
        :param data_index: 比较的数据的下标
        :return: 0为相同，1为新数据更大，2为新数据更小
        """
        if self.__inside_data_list[data_index] == self.outside_data_list[data_index]:
            return 0
        elif self.__inside_data_list[data_index] < self.outside_data_list[data_index]:
            return 1
        else:
            return 2

    def update_data(self):
        """
        在循环的最后更新旧版数据，并获得下一轮的轮次
        """
        self.__inside_data_list.clear()
        self.__inside_data_list = self.outside_data_list.copy()
        self.outside_data_list[0] += 1
