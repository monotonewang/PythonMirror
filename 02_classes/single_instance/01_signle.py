class MediaPlayer:
    instance = None
    init_flag=False

    @staticmethod
    def play():
        print("I am playing")

    # 保证初始化一次
    def __init__(self):
        if self.init_flag:
            return
        self.init_flag=True
        print("init")

    # 为对象分配内存空间
    def __new__(cls, *args, **kwargs):
        print("new ")

        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


mediaPlayer1 = MediaPlayer()
print(mediaPlayer1)
mediaPlayer2 = MediaPlayer()
print(mediaPlayer2)
