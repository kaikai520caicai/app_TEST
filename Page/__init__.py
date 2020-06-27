class Fa:

    def __init__(self):
        self.name = "不一样的烟火~"

    def get_name(self):
        print(self.name)


class So(Fa):

    def __init__(self):
        # super().__init__()  # 初始化父类init
        Fa.__init__(self)  # 初始化父类init

    def use_fa_func(self):
        """使用Fa类的get_name方法"""
        print("我就是我~")
        self.get_name()

So().use_fa_func()