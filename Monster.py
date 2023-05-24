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

        # 转化字符串为列表
        str_act_loop = Global_Variable.monster_rule_list[mon_id][5]
        self.act_loop = [int(i) for i in str_act_loop.split(',')]

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
