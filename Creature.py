import pygame


class Creature(pygame.sprite.Sprite):
    """
    这是生物抽象基类
    """
    loc: list[int, int]  # 位置
    is_moving: bool  # 判断自身是否正在移动
    max_blood: int  # 最大血量
    blood: int  # 现有血量
    living: bool  # 是否活着
    attack: int  # 攻击力
    creature_rect: pygame.rect.Rect  # 生物的rect
    direction: int  # 面朝方向，0上，1下，2左，3右
    status: int  # 状态
    img_list: list[list[pygame.Surface]]

    def __init__(self):
        self.living = True
        pass

    def load_img(self, load: str):
        """

        未完成

        大概率不再使用
        需要添加获取位置的方法

        目前应该是仅供类内部使用的函数
        快捷转换图像法
        :param load:
        :return:
        """
        self.image = pygame.image.load(load).convert()
        self.rect = self.image.get_rect()

    def flush_and_get_creature_rect(self):
        """
        用于实例化生物rect属性并返回之
        :return: 生物rect
        """
        self.creature_rect = self.image.get_rect()
        self.creature_rect.top = 50 * (self.loc[0] + 1) - 10 - self.image.get_rect().height
        self.creature_rect.left = 50 * self.loc[1] + 25 - self.image.get_rect().width / 2
        return self.creature_rect

    def flush_status(self, direction, status):
        self.direction = direction
        self.status = status
        self.image = self.img_list[direction][status]
        self.flush_and_get_creature_rect()

    def detect_creature_rounding(self, loc_set: set, the_player: 'Creature'):
        """
        用来侦查周围十字区域有没有生物，以及玩家的位置
        :param loc_set: 当前轮的生物位置集合
        :param the_player: 玩家
        :return: 返回一个bool列表，0上方，1下方，2左方，3右方，以及一个整数，-1表示没有玩家，0表示上方有玩家，以此类推
        """
        loc = self.loc
        rounding_list = [False, False, False, False]
        rounding_player = 0
        loc_0 = [loc[0] - 1, loc[1]]
        loc_1 = [loc[0] + 1, loc[1]]
        loc_2 = [loc[0], loc[1] - 1]
        loc_3 = [loc[0], loc[1] + 1]
        if loc_0 in loc_set:
            rounding_list[0] = True
            if loc_0 == the_player.loc:
                rounding_player = 0
        if loc_1 in loc_set:
            rounding_list[1] = True
            if loc_1 == the_player.loc:
                rounding_player = 1
        if loc_2 in loc_set:
            rounding_list[2] = True
            if loc_2 == the_player.loc:
                rounding_player = 2
        if loc_3 in loc_set:
            rounding_list[3] = True
            if loc_3 == the_player.loc:
                rounding_player = 3
        return rounding_list, rounding_player

    def move(self, direction: int):
        """
        控制运动的函数
        :param direction: 方向，0上，1下，2左，3右
        """
        if direction == 0:
            self.move_up()
        elif direction == 1:
            self.move_down()
        elif direction == 2:
            self.move_left()
        elif direction == 3:
            self.move_right()

    def move_up(self):
        self.loc[0] -= 1
        self.turn_up()

    def move_down(self):
        self.loc[0] += 1
        self.turn_down()

    def move_left(self):
        self.loc[1] -= 1
        self.turn_left()

    def move_right(self):
        self.loc[1] += 1
        self.turn_right()

    def turn(self, direction: int):
        """
                控制转向的函数
                :param direction: 方向，0上，1下，2左，3右
                """
        if direction == 0:
            self.turn_up()
        elif direction == 1:
            self.turn_down()
        elif direction == 2:
            self.turn_left()
        elif direction == 3:
            self.turn_right()

    def turn_up(self):
        self.direction = 0
        self.image = self.img_list[0][self.status]

    def turn_down(self):
        self.direction = 1
        self.image = self.img_list[1][self.status]

    def turn_left(self):
        self.direction = 2
        self.image = self.img_list[2][self.status]

    def turn_right(self):
        self.direction = 3
        self.image = self.img_list[3][self.status]

    def blood_turn_max(self):
        self.blood = self.max_blood

    def die(self):
        self.blood = 0
        pass

    def been_attacked(self, creature: 'Creature', ):
        """
        被攻击处理
        :param creature: 施加攻击的生物
        :param map: 对应map
        """
        self.blood -= creature.attack
        if self.blood <= 0:
            self.die()

    def do_attack(self, creature: 'Creature'):
        """
        攻击处理
        :param creature:遭受攻击的生物
        """
        creature.been_attacked(self)

    def get_last_loc(self):
        """
        获得移动前的位置
        :return:
        """
        if self.direction == 0:
            return (self.loc[0] + 1, self.loc[1])
        elif self.direction == 1:
            return (self.loc[0] - 1, self.loc[1])
        elif self.direction == 2:
            return (self.loc[0], self.loc[1] + 1)
        else:
            return (self.loc[0], self.loc[1] - 1)
