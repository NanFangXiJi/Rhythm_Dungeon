import Creature

class Monster(Creature.Creature):
    mon_id: int  # 怪物编号
    mon_name: str  # 怪物名
    act_mode: list[int]  # 行动模式: 0循环行动 1随机行动 2跟踪行动
    act_loop: list[int]  # 行动循环：0上 1下 ……
    act_loop_len: int  # 行动循环长

    def __init__(self, act_mode):
        super().__init__()
        self.act_mode = act_mode
