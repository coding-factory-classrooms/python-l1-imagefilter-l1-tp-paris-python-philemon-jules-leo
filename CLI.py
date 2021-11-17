import sys
import core

args = sys.argv
print(args)
conf = {
    "input":'',
    'output':'',
    'filters':''
}

for i, arg in enumerate(args):
    if arg == '-i':
        conf["input"] = args[i + 1]
    if arg == '-o':
        conf['output'] = args[i + 1]
    if arg == '-filters':
        conf['filters'] = args[i + 1]

arg_filter = conf['filters']

print(conf)
images = core.get_images(conf["input"])
core.apply_filters(images,conf['output'])