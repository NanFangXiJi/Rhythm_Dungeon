import pygame

import Global_Variable


class Square:
    object_id: int  # 该方格上的物体id
    accessible: bool  # 该方格的可通过性
    graphics: list[pygame.Surface]  # 该方格上物品的贴图列表

    def __init__(self, obj_id: int = 0):
        self.object_id = obj_id
        self.accessible = bool(Global_Variable.obj_rule_list[2])

    def flush_status(self):
        """
        改变物体id后，通过该函数来更新物体信息
        """
        self.accessible = bool(Global_Variable.obj_rule_list[2])
        