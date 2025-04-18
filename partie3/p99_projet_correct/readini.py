import configparser

def data_path():
    cfg = configparser.ConfigParser()
    cfg.read('cfg_reservations.ini')
    return (cfg['directories']["data"])



