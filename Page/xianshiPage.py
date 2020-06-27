from Base.base import Base
from Page.pageElements import PageElements


class XianShiPage(Base):

    def __init__(self):
        super().__init__()

    def choice_ziti(self):
        """选择字体"""
        # 点击字体大小
        self.click_ele(PageElements.xianshi_ziti_dx_xpath)
        # 点击普通
        self.click_ele(PageElements.xianshi_choice_pt_xpath)

    def get_summary_list(self):
        """获取页面所有描述信息"""
        # 获取所有描述信息
        results = self.search_eles(PageElements.xianshi_get_summary_ids)
        return [i.text for i in results]
