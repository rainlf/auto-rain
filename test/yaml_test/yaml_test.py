# -*- coding: utf-8 -*-
import json
from datetime import date

import yaml


def date_handler(obj):
    if isinstance(obj, (date,)):
        return obj.isoformat()  # 将日期对象转换为ISO格式的字符串
    raise TypeError("Type not serializable")


with open('test.yml', 'r', encoding='utf-8-sig') as file:
    data = yaml.safe_load(file)
    print(json.dumps(data, default=date_handler))

with open('test2.yml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
    print(data)
    print(json.dumps(data, ensure_ascii=False, default=date_handler))

