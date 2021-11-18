
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
# def check_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-origine', type=str, help='choose the origin file', default="")
#     parser.add_argument('-i', '--input', help='initiate input argument')
#     parser.add_argument('-output_path', type=str, help='choose the output file', default="")
#     parser.add_argument('-o', '--output', help='initiate output argument')
#     parser.add_argument('-filter_choice', type=str, help='choose the filters you want to use', default="")
#     parser.add_argument('-f', '--filter', help='initiate filters argument')
#     parser.add_argument('-config_file_choice', type=str, help='choose the config_file you want to use', default="")
#     parser.add_argument('-c', '--config_file', help='initiate config_file argument')
#     parser.add_argument('-l', '--log', help='show the whole log file')
#
#     args = parser.parse_args()
#
#     if args.input:
#         print(args.input)
#         print(args.origine)
#         l.log('the argument for the input file has been taken')
#         conf["input"] = args.input
#
#     elif args.output:
#         print(args.output)
#         l.log('the argument for the output file has been taken')
#         conf["output"] = args.output_path
#
#     elif args.filter:
#         l.log('the argument for the filters has been taken')
#         conf["filters"] = args.filter_choice
#
#     elif args.config_file:
#         l.log('the argument for the input file has been taken')
#         config.read(f'{args.config_file_choice}')
#         conf['input'] = config['DEFAULT']['input']
#         conf['output'] = config['DEFAULT']['output']
#         conf['filters'] = config['DEFAULT']['filters']
#
#     elif args.log:
#         l.dump_log()
#
#     else:
#         print('aucun argument spécifié')
#
# if __name__ == '__main__':
#     check_args()



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

# inout existe ?

args_filter = conf['filters']
arg_filter = args_filter.split('|')
images = core.get_images(conf["input"])
core.apply_filters(images,conf['output'], arg_filter)
