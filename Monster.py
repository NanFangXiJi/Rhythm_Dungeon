import Creature

class Monster(Creature.Creature):
    mon_id: int  # 怪物编号
    mon_name: str  # 怪物名
    act_mode: list[int]  # 行动模式: 0循环行动 1随机行动 2跟踪行动
    act_loop: list[int]  # 行动循环：0上 1下 ……
    act_loop_len: int  # 行动循环长
    base: bool  # 表示是否为基

    def __init__(self, mon_id: int):
        super().__init__()
        self.base = True

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
