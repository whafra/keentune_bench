import os
import logging

from configparser import ConfigParser

LOGLEVEL = {
    "DEBUG"     : logging.DEBUG,
    "INFO"      : logging.INFO,
    "WARNING"   : logging.WARNING,
    "ERROR"     : logging.ERROR
}

class Config:
    conf_file_path = "/etc/keentune/conf/bench.conf"
    conf = ConfigParser()
    conf.read(conf_file_path)

    KEENTUNE_HOME      = conf['bench']['KEENTUNE_HOME']
    KEENTUNE_WORKSPACE = conf['bench']['KEENTUNE_WORKSPACE']
    BENCH_PORT         = conf['bench']['BENCH_PORT']

    print("KeenTune Home: {}".format(KEENTUNE_HOME))
    print("KeenTune Workspace: {}".format(KEENTUNE_WORKSPACE))

    FILES_PATH = os.path.join(KEENTUNE_WORKSPACE, "bench-files")

    # log
    LOGFILE_PATH = conf['log']['LOGFILE_PATH']
    _LogPATH = os.path.dirname(LOGFILE_PATH)

    CONSOLE_LEVEL = LOGLEVEL[conf['log']['CONSOLE_LEVEL']]
    LOGFILE_LEVEL = LOGLEVEL[conf['log']['LOGFILE_LEVEL']]
    LOGFILE_INTERVAL = int(conf['log']['LOGFILE_INTERVAL'])
    LOGFILE_BACKUP_COUNT = int(conf['log']['LOGFILE_BACKUP_COUNT'])

    for _PATH in [KEENTUNE_WORKSPACE, FILES_PATH, _LogPATH]:
        if not os.path.exists(_PATH):
            os.makedirs(_PATH)