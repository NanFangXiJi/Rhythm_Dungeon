import Creature
import Global_Variable


class Monster(Creature.Creature):
    mon_id: int  # 怪物编号
    mon_name: str  # 怪物名
    act_mode: list[int]  # 行动模式: 0循环行动 1随机行动 2跟踪行动
    act_loop: list[int]  # 行动循环：0上 1下 ……
    act_loop_len: int  # 行动循环长

    def __init__(self,mon_id):
        super().__init__()
        self.base = True
        self.mon_id = mon_id

        self.mon_name = str(Global_Variable.monster_rule_list[mon_id][1])
        self.act_mode = list(Global_Variable.monster_rule_list[mon_id][2])
        self.act_loop = list(Global_Variable.monster_rule_list[mon_id][5])
        self.act_loop_len = len(list(Global_Variable.monster_rule_list[mon_id][5]))
