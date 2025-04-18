#argparse — Parser for command-line options, arguments and subcommands
"""
OBSOLETE
import sys
print(sys.argv[1])
"""
import argparse

#
def init_config():
    parser = argparse.ArgumentParser(
                        prog='SystemeResa',
                        description='Reservation de Trajets')

    parser.add_argument('filepath', type=str, help='filepath')
    parser.add_argument('-d','--debug', default='yes', help='debug')
    parser.add_argument('-l','--limit', default=20, type=int, help='limit')

    # DECLENCHE
    args = parser.parse_args()
    return args

#configparser — Configuration file parser



#zipfile — Work with ZIP archives


#sqlite3 — DB-API 2.0 interface for SQLite databases