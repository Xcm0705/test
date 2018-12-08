import random
import pygame

# 设置游戏窗口常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
# 设置时钟常量
FRAME_PER_SEC = 60
# 定义敌机定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义子弹定时器
CREATE_FIRE_EVENT = pygame.USEREVENT + 1
# 定义英雄定时器
CREATE_HERO_EVENT = pygame.USEREVENT + 2
CREATE_HERO_EVENT1 = pygame.USEREVENT + 3


# 创建游戏精灵类
class PlaneSprite(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, image_name, speed=1):
        # 继承父类
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置图像位置
        self.rect = self.image.get_rect()
        # 设置初始速度
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


# 创建背景类
class BackGroud(PlaneSprite):
    # 初始化
    def __init__(self, is_alt=False):
        # 继承父类
        super().__init__("./images/background.png")
        # 判断图像是否重叠
        if is_alt:
            self.rect.y = -self.rect.height

    # 速度更新
    def update(self):
        # 继承父类
        super().update()
        # 判断图像是否移出屏幕
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


# 创建敌机类
class Enemy(PlaneSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始速度
        self.speed = random.randint(1, 3)
        # 设置敌机从屏幕顶部飞进来
        self.rect.bottom = 0
        # 设置敌机在横轴的不同位置出现
        self.max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, self.max_x)

    def update(self):
        super().update()
        # 判断敌机是否飞出屏幕
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


# 创建英雄类
class Hero(PlaneSprite):
    def __init__(self, images_name, hero_speed):
        super().__init__(images_name, hero_speed)

        # # 判断两辆英雄飞机是否重叠
        # if is_alt:
        #     self.rect.y = self.rect.height + 0.5

        # 指定英雄的初始位置（centerx = x + width）
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.bottom - 180

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 设置英雄的水平位置
        self.rect.x += self.speed
        # 设置英雄只能在屏幕范围内移动
        if self.rect.x < 0:
            self.rect.x = 0
        # right = x + width
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            # 创建子弹对象
            bullet = Bullet()
            self.bullet_group.add(bullet)
            # 指定子弹的位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y - i*20


# 创建子弹类
class Bullet(PlaneSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕，若是则销毁
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass











