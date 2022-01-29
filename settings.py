class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 浅灰色
        # 飞船设置
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (70, 130, 180)  # 钢蓝色子弹
        self.bullets_allowed = 5
        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏节奏的速度
        self.speedup_scale = 2.0
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    # noinspection PyAttributeOutsideInit
    def initialize_dynamic_settings(self):
        """初始化using游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.1
        self.fleet_direction = 1  # 1表示外星人向右移动, -1代表外星人向左移动
        self.alien_points = 50  # 初始时一个外星人值50分

    def increase_speed(self):
        """提高速度设置和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # noinspection PyAttributeOutsideInit
        self.alien_points = int(self.alien_points * self.score_scale)
