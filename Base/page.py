from Page.settingPage import SettingPage
from Page.xianshiPage import XianShiPage


class Page:
    """返回所有页面实例化对象"""

    @classmethod
    def get_settingPage(cls):
        """返回设置页面类实例化对象"""
        return SettingPage()

    @classmethod
    def get_xianshiPage(cls):
        """返回显示页面类实例化对象"""
        return XianShiPage()
