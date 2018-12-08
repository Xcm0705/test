# import pygame

from plane_sprite import *


# 创建游戏类
class GameMain(object):
    # 初始化
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 设置时钟
        self.clock = pygame.time.Clock()
        # 设置定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_FIRE_EVENT, 600)
        # 设置删除和创建英雄2的时间间距
        pygame.time.set_timer(CREATE_HERO_EVENT, 1000)
        pygame.time.set_timer(CREATE_HERO_EVENT1, 500)
        # 调用私有方法创建精灵
        self.__create_sprites()

    # 创建精灵
    def __create_sprites(self):
        # 创建背景精灵
        bg = BackGroud()
        bg1 = BackGroud(True)
        # 将背景精灵放进精灵组
        self.back_group = pygame.sprite.Group(bg, bg1)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵(英雄要在其他方法里面使用)
        self.hero1 = Hero("./images/me2.png", 0)
        self.hero2 = Hero("./images/me1.png", 0)
        self.hero_group = pygame.sprite.Group(self.hero1, self.hero2)

    # 开始游戏
    def start_game(self):
        print("游戏开始")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handle()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    # 事件监听
    def __event_handle(self):
        # 在event.get()中判断事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机对象
                enemy = Enemy()
                # 每次生成敌机，便将敌机精灵添加进精灵组
                self.enemy_group.add(enemy)
            elif event.type == CREATE_HERO_EVENT:
                # 判断英雄2是否在英雄精灵组内，若在，则移除
                if self.hero2 in self.hero_group:
                    self.hero2.kill()
            elif event.type == CREATE_HERO_EVENT1:
                # 判断英雄2是否在英雄精灵组内，若否，则创建
                if self.hero2 not in self.hero_group:
                    self.hero2 = Hero("./images/me1.png", 0)
                    self.hero_group.add(self.hero2)
                    self.hero2.rect.centerx = self.hero1.rect.centerx
            elif event.type == CREATE_FIRE_EVENT:
                # 让英雄来调用发射子弹方法
                self.hero1.fire()
                self.hero2.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero1.speed = 2
            self.hero2.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero1.speed = -2
            self.hero2.speed = -2
        else:
            self.hero1.speed = 0
            self.hero2.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero1.bullet_group, self.enemy_group, True, True)
        # 英雄与敌机碰撞摧毁
        enemies = pygame.sprite.spritecollide(self.hero1, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero1.kill()
            self.__game_over()
        pass

    # 更新绘制精灵组
    def __update_sprites(self):
        # 更新精灵组
        self.back_group.update()
        # 绘制精灵组于屏幕上
        self.back_group.draw(self.screen)

        # 更新敌机精灵
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 更新英雄精灵
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 更新子弹精灵
        self.hero1.bullet_group.update()
        self.hero1.bullet_group.draw(self.screen)

    # 结束游戏
    @staticmethod
    def __game_over():
        print("游戏结束")
        # 卸载所有模块
        pygame.quit()
        # 退出程序
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = GameMain()
    # 调用开始游戏方法
    game.start_game()
