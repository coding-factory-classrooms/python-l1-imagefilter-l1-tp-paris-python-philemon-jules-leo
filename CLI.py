
import core
import logger as l
import configparser
import argparse

config = configparser.ConfigParser()

config.read('config.ini')


conf = {"input": '',
        'output': '',
        'filters': '',
        'log_file': config['DEFAULT']['log_file'],
        'type': '',
        'output_video':'',
        }

l.init_log(conf['log_file'])

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', type=str, help='initiate input argument')
parser.add_argument('-o', '--output', type=str,  help='initiate output argument')
parser.add_argument('-f', '--filters', type=str, help='initiate filters argument')
parser.add_argument('-c', '--config_file', type=str,  help='initiate config_file argument')
parser.add_argument('-l', '--log', type=str,  help='show the whole log file')
parser.add_argument('-d', '--display_filters', type=str,  help='show the filters available')
parser.add_argument('-v', '--video', type=str,  help='show the filters available')
parser.add_argument('-O', '--output_video', type=str,  help='show the filters available')
parser.add_argument('-g', '--gif', type=str,  help='transform the given image in gif')


args = parser.parse_args()

if args.config_file:

    l.log('the argument for the config file has been taken')
    config.read(f'{args.config_file}')
    conf['input'] = config['DEFAULT']['input']
    conf['output'] = config['DEFAULT']['output']
    conf['filters'] = config['DEFAULT']['filters']

if args.input:

    l.log('the argument for the input file has been taken')
    conf["input"] = args.input

if args.output:

    l.log('the argument for the output file has been taken')
    conf["output"] = args.output

if args.filters:
    l.log('the argument for the filters has been taken')
    conf["filters"] = args.filters

if args.log:
    l.dump_log()

if args.display_filters:
    l.log('diplaying filters')
    print("available filters: grayscale | zeTeam | dilate:* | blur:* , replace * with a number to adjust filter intensity")

if args.output_video:
    l.log('the argument for the output_video file has been taken')
    conf['output_video']= args.output_video

if args.video:
    if conf['output_video'] != '':
        core.get_video(args.video, conf['output_video'])
        if args.filters:
            l.log('the argument for the filters has been taken')
            config.read(f'config.ini')
            conf['filters'] = args.filters
            args_filter = conf['filters']
            arg_filter = args_filter.split('|')
            conf['input'] = core.get_image_video(conf['output_video'])
            image = conf['input']
            core.apply_filters(image, conf['output'], arg_filter)
        else:
            print('the filters argument is missing')
    else:
        print('the argument for the output_video file is missing')

if args.gif:
    core.make_gif(conf['output'], args.gif)

else:
    args_filter = conf['filters']
    arg_filter = args_filter.split('|')
    images = core.get_images(conf["input"])
    core.apply_filters(images, conf['output'], arg_filter)



# inout existe ?

