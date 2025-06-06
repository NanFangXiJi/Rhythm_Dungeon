import pygame.image

import Creature
import Global_Variable


class Player(Creature.Creature):
    def __init__(self, init_loc: list[int, int], direction: int = 1, status: int = 1):
        """
        :param init_loc: 地图需要给出的初始位置
        """
        super().__init__()
        self.loc = init_loc
        self.img_list = [[pygame.image.load('img/character/U1.png'),
                          pygame.image.load('img/character/U2.png'),
                          pygame.image.load('img/character/U3.png')],
                         [pygame.image.load('img/character/D1.png'),
                          pygame.image.load('img/character/D2.png'),
                          pygame.image.load('img/character/D3.png')],
                         [pygame.image.load('img/character/L1.png'),
                          pygame.image.load('img/character/L2.png'),
                          pygame.image.load('img/character/L3.png')],
                         [pygame.image.load('img/character/R1.png'),
                          pygame.image.load('img/character/R2.png'),
                          pygame.image.load('img/character/R3.png')]]
        self.image = self.img_list[direction][status]
        self.flush_and_get_creature_rect()
        self.direction = direction
        self.status = status
        self.attack = Global_Variable.init_attack_of_player
        self.max_blood = Global_Variable.init_max_blood_of_player
        self.blood = self.max_blood

