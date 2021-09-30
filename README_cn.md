[English](./keentune-bench/README.md)| [简体中文](./keentune-bench/README_ch.md) 

# KeenTune Bench  

## 简介
---  
KeenTune-bench 是用来控制基准运行程序（Benchmark）的组件，部署在Benchmark所在环境。该组件主要用于执行Benchmark和获取评价指标。

## 安装方法
---  
### 1. 安装 python-setuptools
```sh
$ sudo apt-get install python-setuptools
or
$ sudo yum install python-setuptools
```

### 2. 安装 keentune-bench
```shell
$ sudo python3 setup.py install
```

### 3. 安装 requirements
```shell
$ pip3 install -r requirements.txt
```

### 4. 运行 keentune-bench
```shell
$ keentune-bench
```

## 代码结构
---  
+ common: 通用方法模块
+ controller: Web通信模块
+ modules: 功能模块

## Documentation