import yaml

with open("data1.yaml", "r", encoding="utf-8")as f:
    data = yaml.safe_load(f)
    print("返回的数据:", data)
    # print("返回的数据类型:", type(data.get("info")))
