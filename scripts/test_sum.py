import pytest
import yaml, os
from Base.getData import GetData


def sum_data():
    # 空列表 存储测试数据
    sum_list = []
    # 读取yaml文件数据
    data = GetData.get_yaml_data("sum.yml")
    for i in data.values():
        # 添加元组数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list


class TestSum:
    @pytest.mark.parametrize("a,b,c", sum_data())
    def test_sum(self, a, b, c):
        """判断两个数之和 等于 第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
