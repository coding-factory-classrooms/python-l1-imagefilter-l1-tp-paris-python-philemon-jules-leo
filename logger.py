from datetime import datetime


log_file = None

def init_log(log_filepath):
    """
    fonction qui recupère le nom du log_file dans le fichier ini
    :param log_filepath: le nom du fichier recupérer dans le fichier ini
    """
    global log_file
    log_file = log_filepath

def log(msg):
    """
    fonction qui permet de logguer le msg donné dans le log_file
    :param msg:  msg a logguer
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    print(formatted)
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')

def dump_log():
    """
    fonction permettant d'afficher l'intégralité du log_file
    """
    try:
        with open(log_file, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f'Cannot open {log_file}. error={e}')


