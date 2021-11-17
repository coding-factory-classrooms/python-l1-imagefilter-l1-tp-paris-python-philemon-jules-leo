from datetime import datetime
import configparser
from CLI import conf

config = configparser.ConfigParser()
config.read()
log_file = conf['log_file']

def log(msg):

    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    print(formatted)
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')

def dump_log():

    try:
        with open(log_file, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f'Cannot open {log_file}. error={e}')


