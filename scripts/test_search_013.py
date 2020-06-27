from appium import webdriver
import pytest, time
from selenium.webdriver.common.by import By
from Base.base import Base


class Test_Search:

    def setup_class(self):
        """声明driver"""
        # server 启动参数
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'sanxing',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings'
        }

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 实例化Base类
        self.base_obj = Base(self.driver)

        # 页面元素
        # 搜索按钮
        self.search_btn_id = (By.ID, "com.android.settings:id/search")
        # 搜索输入框
        self.search_input_id = (By.ID, "android:id/search_src_text")
        # 搜索结果
        self.search_result_ids = (By.ID, "com.android.settings:id/title")

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮 并且 点击一次"""
        self.base_obj.click_ele(self.search_btn_id)

    @pytest.mark.parametrize("search_data, exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_text(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 输入框输入内容
        self.base_obj.send_ele(self.search_input_id, search_data)
        # 获取结果
        results = self.base_obj.search_eles(self.search_result_ids)
        # 断言
        assert exp_data in [i.text for i in results]
