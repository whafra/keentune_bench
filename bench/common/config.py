import os
import logging

from configparser import ConfigParser

LOGLEVEL = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR
}


class Config:
    conf_file_path = "/etc/keentune/conf/bench.conf"
    conf = ConfigParser()
    conf.read(conf_file_path)

    keentune_home = conf['home']['keentune_home']
    print("KeenTune Home: {}".format(keentune_home))
    keentune_workspace = conf['home']['keentune_workspace']
    print("KeenTune Workspace: {}".format(keentune_workspace))
    
    bench_port = conf['bench']['bench_port']
    tmp_dir = os.path.join(keentune_workspace,"tmp")
    files_dir = os.path.join(keentune_workspace, "files")
    
    # log
    logfile_path = conf['log']['logfile_path']
    console_level = LOGLEVEL[conf['log']['console_level']]
    logfile_level = LOGLEVEL[conf['log']['logfile_level']]
    logfile_interval = int(conf['log']['logfile_interval'])
    logfile_backup_count = int(conf['log']['logfile_backup_count'])

    if not os.path.exists(keentune_workspace):
        os.makedirs(keentune_workspace)

    if not os.path.exists(files_dir):
        os.makedirs(files_dir)
        
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)