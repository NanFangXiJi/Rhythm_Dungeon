import pygame


class Square:
    object_id: int  # 该方格上的物品id
    accessible: bool  # 该方格的可通过性
    graphics: list[pygame.Surface]  # 该方格上物品的贴图列表

    def __init__(self, obj_id: int):
        self.object_id = obj_id

    def flush_status(self):
        pass
