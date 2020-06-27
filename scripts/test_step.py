import allure


class Test:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤01")
    def test01(self):
        """
        ces步骤
        :return:
        """
        allure.attach("测试步骤为:登录,注册,验证", "附件信息")

    @allure.severity(allure.severity_level.NORMAL)
    def test02(self):
        assert True
