
from Base.driver import Driver
from Base.page import Page

class TestSetZiTi:

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    def test_set_ziti(self):
        # 设置页面 -点击显示
        Page.get_settingPage().click_xianshi_btn()
        # 显示页面 -选择字体
        Page.get_xianshiPage().choice_ziti()
        # 显示页面 -获取描述信息-断言
        assert "普通" in Page.get_xianshiPage().get_summary_list()

