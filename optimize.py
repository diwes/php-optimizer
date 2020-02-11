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

if len(sys.argv) > 2:
    if (sys.argv[2].lower() == "--append"):
        config['AppendFile'] = 1

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

if config['AppendFile']:
    output_file = open(output, "a+")
else:
    output_file = open(output, "w+")

if config['MultiSpaces']:
    output_file.write("\n<?php\n\n")
else:
    output_file.write("\n<?php\n")


for cc in code:
    if "print>" in cc:
        other_param = cc.replace("print>", "")
        if config['MultiSpaces']:
            output_file.write("\n\nprint \"" + code[cc] + "\";\n")
        else:
            output_file.write("print \"" + code[cc] + "\";\n")
    if "interface>" in cc:
        name_class = cc.replace("interface>", "")
        if config['MultiSpaces']:
            output_file.write("\ninterface " + name_class + "\n{\n\n\n}\n")
        else:
            output_file.write("\ninterface " + name_class + "{}\n")
    if "classabs>" in cc:
        name_class = cc.replace("classabs>", "")
        if config['MultiSpaces']:
            output_file.write("\nabstract class " + name_class + "\n{\n\n\n}\n")
        else:
            output_file.write("\nabstract class " + name_class + "{}\n")
    if "classfinal>" in cc:
        name_class = cc.replace("classfinal>", "")
        if config['MultiSpaces']:
            output_file.write("\nfinal class " + name_class + "\n{\n\n\n}\n")
        else:
            output_file.write("\nfinal class " + name_class + "{}\n")
    if "class>" in cc:
        name_class = cc.replace("class>", "")
        if config['MultiSpaces']:
            output_file.write("\nclass " + name_class + "\n{\n\n\n}\n")
        else:
            output_file.write("\nclass " + name_class + "{}\n")
    if "function>" in cc:
        name_function = cc.replace("function>", "")
        if config['MultiSpaces']:
            output_file.write("\nfunction " + name_function + "(" + code[
                cc] + ") {\n" + "\t// Enter code your function " + name_function + "\n}\n")
        else:
            output_file.write("function " + name_function + "(" + code[
                cc] + ") {\n" + "\t// Enter code your function " + name_function + "\n}\n")
    if "var>" in cc:
        if type(code[cc]) == str:
            output_file.write("$" + cc.replace("var>", "") + " = \"" + str(code[cc]) + "\";\n")
        else:
            output_file.write("$" + cc.replace("var>", "") + " = " + str(code[cc]) + ";\n")

if ("laravel" in optimizer['optimize']):
    for cc in code:
        if "route:get>" in cc:
            other_param = cc.replace("route:get>", "")
            output_file.write("\nRoute::get('" + other_param + "', " + code[cc] + ");\n")
        if "route:post>" in cc:
            other_param = cc.replace("route:post>", "")
            output_file.write("\nRoute::post('" + other_param + "', " + code[cc] + ");\n")

if config['MultiSpaces']:
    output_file.write("\n?>\n")
else:
    output_file.write("\n?>")

output_file.close()

# End

print(colored("Well done, check is", "green") + " " + colored(output, "yellow"))
