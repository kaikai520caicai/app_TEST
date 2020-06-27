from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""

    # ----搜索页面元素----
    # 搜索按钮
    search_btn_id = (By.ID, "com.android.settings:id/search")
    # 搜索输入框
    search_input_id = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result_ids = (By.ID, "com.android.settings:id/title")

    # ----设置页面----
    # 显示
    setting_xianshi_btn_xpath = (By.XPATH, "//*[contains(@text,'显示')]")

    # ----显示页面---
    # 字体大小
    xianshi_ziti_dx_xpath = (By.XPATH, "//*[contains(@text,'字体大小')]")
    # 选择字体
    xianshi_choice_pt_xpath = (By.XPATH, "//*[contains(@text,'普通')]")
    # 描述信息
    xianshi_get_summary_ids = (By.ID, "android:id/summary")
