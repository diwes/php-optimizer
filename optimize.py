import errno

import yaml
import os
import sys

from termcolor import colored

# Open file optimizer
optimizer = open(sys.argv[1] + ".yaml", "r")
optimizer = yaml.load(optimizer, Loader=yaml.FullLoader)

# Init vars
filename = optimizer['filename']
output = optimizer['output']

code = optimizer['start']
optimizes = optimizer['optimize']

# OutPut
if not os.path.exists(os.path.dirname(output)):
    try:
        os.makedirs(os.path.dirname(output))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

output_file = open(output, "a+")

output_file.write("\n<?php\n\n")

for cc in code:
    if "function>" in cc:
        name_function = cc.replace("function>", "")
        output_file.write("\nfunction " + name_function + "(" + code[cc] + ") {\n" + "\t// Enter code your function " + name_function + "\n}\n")
    if "var>" in cc:
        if type(code[cc]) == str:
            output_file.write("$" + cc.replace("var>", "") + " = \"" + str(code[cc]) + "\";\n")
        else:
            output_file.write("$" + cc.replace("var>", "") + " = " + str(code[cc]) + ";\n")

output_file.write("\n?>\n")

output_file.close()

# End

print(colored("Well done, check is", "green") + " " + colored(output, "yellow"))
