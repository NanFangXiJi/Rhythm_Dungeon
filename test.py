import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

alpha = 0
alpha_increment = 1  # 每帧透明度增加的值

white_bg = (255, 255, 255)  # 白色背景

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    alpha += alpha_increment  # 增加透明度

    if alpha >= 255:
        alpha = 255  # 限制透明度最大值为255

    screen.fill(white_bg)  # 填充白色背景

    black_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)  # 创建与屏幕大小相同的表面，带有alpha通道
    black_overlay.fill((0, 0, 0, alpha))  # 填充为带有透明度的黑色

    screen.blit(black_overlay, (0, 0))  # 绘制黑色覆盖层到屏幕上

    pygame.display.flip()
    clock.tick(60)
