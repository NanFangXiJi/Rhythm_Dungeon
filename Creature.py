import pygame


class Creature(pygame.sprite.Sprite):
    """
    这是生物抽象基类
    """
    loc: list[int, int]  # 位置
    creature_rect: pygame.rect.Rect  # 生物的rect
    direction: int  # 面朝方向，0上，1下，2左，3右
    status: int  # 状态
    img_list: list[list[pygame.Surface]]

    def __init__(self):
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

    def move(self, direction: int):
        """

        未完成

        控制运动的函数
        :param direction: 方向，0上，1下，2左，3右
        :return:
        """

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
