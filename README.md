# KeenTune Bench  
## Introduction
---  
KeenTune-bench is a benchmark controlling components, which is deployed with benchmark tools. It is used in dynamic tuning workflows to run benchmark tools and get evalation metrics.

## Build & Install
### By setuptools
Setuptools can build KeenTune-bench as a python lib. We can run setuptools as  
```s
>> pip3 install setuptools
>> python3 setup.py install
```

### By pyInstaller
pyInstaller can build KeenTune-bench as a binary file. We can run pyInstaller as  
```s
>> pip3 install pyInstaller
>> make
>> make install
```

### Configuration
After install KeenTune-bench by setuptools or pyInstaller, we can find configuration file in **/etc/keentune/conf/bench.conf**
```conf
[agent]
KEENTUNE_HOME = /etc/keentune/                  # KeenTune-bench install path.
KEENTUNE_WORKSPACE = /var/keentune/             # KeenTune-bench user file workspace.
BENCH_PORT = 9874                               # KeenTune-bench listening port.

[log]
CONSOLE_LEVEL = ERROR                           # Log level of console.
LOGFILE_LEVEL = DEBUG                           # Log level of logfile.
LOGFILE_PATH  = /var/log/keentune/bench.log     # Logfile saving path.
LOGFILE_INTERVAL = 1                            
LOGFILE_BACKUP_COUNT = 14
```

### Run
After modify KeenTune-bench configuration file, we can deploy KeenTune-bench and listening to requests as 
```s
>> keentune-bench
```
or depoly KeenTune-bench by systemctl  
```s
>> systemctl start keentune-bench
```