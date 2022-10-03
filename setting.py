class Settings:

    def __init__(self):
        """初始化各项设置"""
        self.game_name = "星玄"
        self.ship = (1600, 900)
        self.image = 'Material\\image\\icon.bmp'  # 背景图片路径
        self.word_path = "Material\\word_body\\simkai.ttf"  # 字体文件路径
        self.word_color = (255, 128, 128)  # 字体颜色
        self.fps = 50  # 刷新率

        #  从相关管理模块抓取信息
        #  种子管理模块
        self.bt_much = 20  # 注：个数从零开始若为4则实际有5个
        self.bt_information = []
