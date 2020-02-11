import errno

import yaml
import os
import sys

from termcolor import colored

# Open file optimizer
optimizer = open(sys.argv[1] + ".yaml", "r")
optimizer = yaml.load(optimizer, Loader=yaml.FullLoader)

# load config
config = open("config.yml", "r")
config = yaml.load(config, Loader=yaml.FullLoader)

# Init vars
filename = optimizer['filename']
output = optimizer['output']

code = optimizer['start']
optimizes = optimizer['optimize']

print(config)

print(optimizer)