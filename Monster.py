import Creature

class Monster(Creature.Creature):

    act_mode: list[int]  # 行动模式: 0循环行动 1随机行动 2跟踪行动

    def __init__(self, act_mode):
        super().__init__()
        self.act_mode = act_mode
