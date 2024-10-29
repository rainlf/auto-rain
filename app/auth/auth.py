# -*- coding: UTF-8 -*-
import oathtool
import pyperclip

from utils import yaml_utils

file = 'rain.config.yml'

config = yaml_utils.load_yaml(file)
print(config)
password = config['password']
token = config['token']
code = oathtool.generate_otp(token)
auth_code = password + " " + code
pyperclip.copy(auth_code)
print("success")
# print(auth_code)
