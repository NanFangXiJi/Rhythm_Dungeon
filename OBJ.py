import pygame

import Global_Variable
import basic_func


class obj:
    object_id: int  # 物体id
    accessible: bool  # 物体可通过性
    destroy_level: int  # 物体的摧毁等级
    layer_for_obj: int  # 物体的地图层内所属层
    size: tuple[int, int]  # 物体的贴图大小
    graphics: list[pygame.Surface] | None  # 物品的贴图列表

    def __init__(self, obj_id: int):
        """
        obj的构造函数
        :param obj_id: 物体id
        """
        self.object_id = obj_id
        self.accessible = bool(Global_Variable.obj_rule_list[obj_id][2])
        self.destroy_level = Global_Variable.obj_rule_list[obj_id][4]
        self.size = (Global_Variable.obj_rule_list[obj_id][5], Global_Variable.obj_rule_list[obj_id][6])
        self.layer_for_obj = Global_Variable.obj_rule_list[obj_id][7]
        # 加载物品贴图列表
        self.graphics = list()
        drw_lst = basic_func.obj_graphics_calculate(Global_Variable.obj_rule_list[obj_id][3])
        if drw_lst[0][0] == 'EMP':
            self.graphics = None
        else:
            for i in range(len(drw_lst)):
                new_surface = pygame.Surface(self.size, pygame.SRCALPHA)
                new_surface.fill((0, 0, 0, 0))
                for j in range(len(drw_lst[i])):
                    img_sur = pygame.image.load('img/obj/' + drw_lst[i][j] + '.png')
                    img_sur_rect = img_sur.get_rect()
                    img_sur_rect.left = 0  # 左边靠左
                    img_sur_rect.top = self.size[1] - img_sur_rect.height  # 底部靠底
                    new_surface.blit(img_sur, img_sur_rect)
                self.graphics.append(new_surface)
