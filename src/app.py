import os
import sys

from utils.log_utils import log
from config.yaml_config import YamlConfig
import utils.file_utils as file_utils


print(file_utils.get_file_path('test.yml'))
config = YamlConfig(file_utils.get_file_path('test.yml'))
print(config.data)
