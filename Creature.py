import pygame


class Creature(pygame.sprite.Sprite):
    """
    这是生物抽象基类
    """
    loc: list[int, int]  # 位置
    img_list: list[list[pygame.Surface]]

    def __init__(self):
        pass

    def load_img(self, load: str):
        """

        未完成
        需要添加获取位置的方法

        目前应该是仅供类内部使用的函数
        快捷转换图像法
        :param load:
        :return:
        """
        self.image = pygame.image.load(load).convert()
        self.rect = self.image.get_rect()

    def move(self, direction: int):
        """

        未完成

        控制运动的函数
        :param direction: 方向，0上，1下，2左，3右
        :return:
        """

    def move_up(self):
        self.loc[0] += 1

    def move_down(self):
        self.loc[0] -= 1

    def move_left(self):
        self.loc[1] -= 1

    def move_right(self):
        self.loc[1] += 1
