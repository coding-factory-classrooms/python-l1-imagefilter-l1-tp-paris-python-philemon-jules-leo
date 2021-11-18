import sys
import core
import logger as l
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

args = sys.argv

conf = {"input": '',
        'output': '',
        'filters': '',
        'log_file': config['DEFAULT']['log_file']
        }

l.init_log(conf['log_file'])

for i, arg in enumerate(args):
    if arg == '-i':
        l.log('the argument for the input file has been taken')
        conf["input"] = args[i + 1]
    if arg == '-o':
        l.log('the argument for the outpout file has been taken')
        conf['output'] = args[i + 1]
    if arg == '-filters':
        l.log('the argument for the filters has been taken')
        conf['filters'] = args[i + 1]
    if arg == '-log':
        l.dump_log()
    if arg == '--config-file':
        l.log('the arguments used are those of the config file')
        config.read(f'{args[i+1]}')
        conf['input'] = config['DEFAULT']['input']
        conf['output'] = config['DEFAULT']['output']
        conf['filters'] = config['DEFAULT']['filters']
    if arg == '-display_filters':
        l.log('diplaying filters')
        print("available filters: grayscale | dilate:* | blur:* , replace * with a number to adjust filter intensity")

# inout existe ?

args_filter = conf['filters']
arg_filter = args_filter.split('|')
images = core.get_images(conf["input"])
core.apply_filters(images,conf['output'], arg_filter)