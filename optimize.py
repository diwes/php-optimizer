import yaml
import os
import sys

optimizer = open(sys.argv[1] + ".yaml", "r")
optimizer = yaml.load(optimizer, Loader=yaml.FullLoader)

print(optimizer)