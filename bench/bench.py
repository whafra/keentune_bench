import tornado

from bench.controller.sendfile import SendfileHandler
from bench.controller.benchmark import BenchmarkHandler
from bench.controller.status import StatusHandler

from bench.common import pylog
from bench.common.config import Config


""" 
KeenTune-bench main function.  

KeenTune-bench running in an auxiliary environment distinguished from tunning target environment.

This environment is used for running benchmark script to target environment to calculate the performance score of target environment with specified parameter configuration
"""


def main():
    pylog.init()

    app = tornado.web.Application(handlers=[
        (r"/sendfile", SendfileHandler),
        (r"/benchmark", BenchmarkHandler),
        (r"/status", StatusHandler)
    ])
    app.listen(Config.bench_port)
    print("KeenTune bench running...")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
