
import core
import logger as l
import configparser
import argparse
import sys

config = configparser.ConfigParser()

config.read('config.ini')


conf = {"input": '',
        'output': '',
        'filters': '',
        'log_file': config['DEFAULT']['log_file'],
        'type':''
        }

l.init_log(conf['log_file'])
args = sys.argv




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
    if arg == '--output-type':
        if args[i + 1] == 'gif':
            conf['type'] = args[i + 1]
            core.make_gif(conf['output'])
        else:
            print('Invalid document type. Accepted document types: gif')
    if arg == '--config-file':
        l.log('the arguments used are those of the config file')
        config.read(f'{args[i+1]}')
        conf['input'] = config['DEFAULT']['input']
        conf['output'] = config['DEFAULT']['output']
        conf['filters'] = config['DEFAULT']['filters']
        for i, arg in enumerate(args):
            if arg == '-i':
                l.log('the argument for the input file has been taken')
                conf["input"] = args[i + 1]
            elif arg == '-o':
                l.log('the argument for the output file has been taken')
                conf['output'] = args[i + 1]
            elif arg == '-filters':
                print('je suis passé par la')
                l.log('the argument for the filters has been taken')
                conf['filters'] = args[i + 1]
    if arg == '-display_filters':
        l.log('diplaying filters')
        print("available filters: grayscale | zeTeam | dilate:* | blur:* , replace * with a number to adjust filter intensity")

    if arg == '-video':
        core.get_video(args[i + 1])
        if args[i + 2] == '-filters':
            l.log('the argument for the filters has been taken')
            config.read(f'config.ini')
            conf['output'] = config['DEFAULT']['output']
            conf['filters'] = args[i + 3]
            args_filter = conf['filters']
            arg_filter = args_filter.split('|')
            conf['input'] = core.get_image_video('output_video')
            image = conf['input']
            core.apply_filters(image, conf['output'], arg_filter)
        else:
            print('the filters argument is missing')


# inout existe ?

# args_filter = conf['filters']
# arg_filter = args_filter.split('|')
# images = core.get_images(conf["input"])
# core.apply_filters(images,conf['output'], arg_filter)