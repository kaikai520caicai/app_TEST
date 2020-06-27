from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def click_xianshi_btn(self):
        """点击显示按钮"""
        self.click_ele(PageElements.setting_xianshi_btn_xpath)

