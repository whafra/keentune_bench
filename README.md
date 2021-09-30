[English](./keentune-bench/README.md)| [简体中文](./keentune-bench/README_ch.md) 

# KeenTune Bench  

## Introduction
---  
KeenTune-bench is a benchmark controlling components, which is deployed with benchmark tools. It is used in dynamic tuning workflows to run benchmark tools and get evalation metrics.


## Installation
---  
### 1. install python-setuptools
```sh
$ sudo apt-get install python-setuptools
or
$ sudo yum install python-setuptools
```

### 2. install keentune-bench
```shell
$ sudo python3 setup.py install
```

### 3. install requirements
```shell
$ pip3 install -r requirements.txt
```

### 4. Run keentune-bench
```shell
$ keentune-bench
```

## Code structure
---  
+ common: common methods
+ controller: Web communication module.
+ modules: Function module

## Documentation