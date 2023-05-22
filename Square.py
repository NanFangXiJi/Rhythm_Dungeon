import pygame

import Global_Variable
import OBJ


class Square:
    obj_on: OBJ.obj  # 方格上的物体
    obj_status: int  # 方格上物体的状态
    square_loc: tuple[int, int]  # 方格在地图上的位置
    square_rect: pygame.rect  # 方格的rect

    def __init__(self, loc: tuple[int, int], obj_id: int = 3, status_id: int = 0):
        self.square_loc = loc
        self.obj_on = Global_Variable.obj_list[obj_id]
        self.obj_status = status_id
        self.square_rect = self.get_rect()

    def get_graphic(self):
        if self.obj_on.graphics is not None:
            return self.obj_on.graphics[self.obj_status]

    def get_rect(self):
        """
        获取Square自身应有的rect的方法
        :return: 自身应有的rect
        """
        pic = self.get_graphic()
        if pic is None:
            return None
        else:
            rect = pic.get_rect()
            rect.left = 50*self.square_loc[1]
            rect.top = 50*(self.square_loc[0] + 1) - rect.height
            return rect
