import pygame

# https://www.pygame.org/contribute.html

pygame.init()
rect = pygame.Rect(100, 200, 125, 335)

print("hero location=%d %d" % (rect.x, rect.y))
print("hero width height=%d %d" % (rect.width, rect.height))

# 创建游戏窗口
while True:
    # 指定屏幕宽度和高度
    pygame.display.set_mode((480, 700))

pygame.quit()
