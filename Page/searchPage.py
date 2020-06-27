
from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self):
        super().__init__()  # 初始化Base类init

    def click_search_btn(self):
        """点击搜索按钮方法"""
        self.click_ele(PageElements.search_btn_id)

    def search_text(self, text):
        """
        搜索内容方法
        :param text: 搜索输入文本内容
        :return:
        """
        self.send_ele(PageElements.search_input_id, text)

    def get_search_result(self):
        """获取搜索结果方法"""
        # 定位搜索结果
        results = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in results]
