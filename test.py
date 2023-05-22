import pygame

# 初始化 Pygame
pygame.init()

# 创建窗口
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载图像
image = pygame.image.load("image.png")
image_width = image.get_width()
image_height = image.get_height()

# 初始放大比例
scale = 1.0

# 循环事件处理
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 放大比例增加
    scale += 0.01

    # 缩放图像
    scaled_image = pygame.transform.scale(image, (int(image_width * scale), int(image_height * scale)))

    # 计算图像位置使其保持中心不变
    x = (screen_width - scaled_image.get_width()) // 2
    y = (screen_height - scaled_image.get_height()) // 2

    # 绘制图像
    screen.fill((0, 0, 0))  # 清空屏幕
    screen.blit(scaled_image, (x, y))

    pygame.display.flip()

# 退出 Pygame
pygame.quit()
