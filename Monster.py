import pygame.image

import Creature
import Global_Variable


class Monster(Creature.Creature):
    mon_id: int  # 怪物编号
    mon_name: str  # 怪物名
    act_mode: list[int]  # 行动模式: 0循环行动 1随机行动 2跟踪行动
    act_loop: list[int]  # 行动循环：0上 1下 ……
    act_loop_len: int  # 行动循环长
    base: bool  # 表示是否为基

    def __init__(self, mon_id):
        super().__init__()
        self.base = True
        self.mon_id = mon_id
        self.mon_name = Global_Variable.monster_rule_list[mon_id][1]
        self.act_mode = Global_Variable.monster_rule_list[mon_id][2]
        self.max_blood = Global_Variable.monster_rule_list[mon_id][3]
        self.attack = Global_Variable.monster_rule_list[mon_id][18]

        # 转化字符串为列表
        str_act_loop = Global_Variable.monster_rule_list[mon_id][5]
        self.act_loop = [int(i) for i in str_act_loop.split(',')]

        # 读取绘制方法字符串，并load
        self.img_list = list()
        cmt1_img_list = 0
        cmt2_img_list = 0
        img_filename_list = list()
        for i in range(6, 18):
            img_filename_list.append(Global_Variable.monster_rule_list[mon_id][i])
        for filename in img_filename_list:
            img_path = f"img/character/{filename}.png"
            img = pygame.image.load(img_path)

            # img_list中二维列表储存
            self.img_list[cmt2_img_list].append(pygame.image.load(img))

            # 处理索引
            if cmt1_img_list == 2:
                cmt1_img_list = 0
                cmt2_img_list += 1
            cmt1_img_list += 1

        self.act_loop_len = len(self.act_loop)

    def copy_base_in_list(self, init_loc: list[int, int], direction: int = 1, status: int = 1):
        """

        未完成，依赖于构造函数

        用于从基中生成可供使用的monster
        :return:新的monster
        """
        mon = Monster(self.mon_id)
        mon.loc = init_loc
        mon.direction = direction
        mon.status = status
        mon.base = False
        return mon
