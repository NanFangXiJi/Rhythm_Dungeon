import Creature

class Player(Creature.Creature):
    def __init__(self, init_loc: list[int, int]):
        """

        未完成

        :param init_loc: 地图需要给出的初始位置
        """
        super().__init__()
        self.loc = init_loc

