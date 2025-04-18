import configparser

cfg = configparser.ConfigParser()

cfg.read('cfg_reservations.ini')
print(cfg.sections())

print(cfg['directories']["data"])



