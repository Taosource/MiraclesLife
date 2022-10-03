class Settings:

    def __init__(self):
        """初始化各项设置"""
        self.game_name = "星玄"
        self.ship = (1600, 900)
        self.image = 'Material\\image\\icon.bmp'  #  背景图片路径
        self.word_path = "Material\\word_body\\simkai.ttf"  # 字体文件路径
        self.word_color = (255, 128, 128)  #  字体颜色
        self.fps = 50  #  刷新率
        self.bt_much = 0
