import re
import os
import sys

from bench.common.system import sysCommand
from bench.common.pylog import functionLog
from bench.common.config import Config

@functionLog
def runBenchmark(benchmark_cmd: str):
    """ run benchmark script.

    Try to import Benchmark class and call method Benchmark.run() if script is end with .py.

    Args:
        benchmark_cmd (str): run benchmark command.

    Returns:
        str: benchmark result or error message.
    """
    python3_pattern = re.compile(r'python3 (.*\.py) (.*)')

    if re.search(python3_pattern, benchmark_cmd):
        python_path = re.search(python3_pattern, benchmark_cmd).group(1)
        ip = re.search(python3_pattern, benchmark_cmd).group(2)

        suc, res = runPyBenchmark(python_path, ip)
        if suc:
            return True, res

    suc, res = sysCommand(benchmark_cmd)
    if suc:
        return True, res

    else:
        return False, "Execute the Benchmark script {} failed:{}".format(benchmark_cmd, res)


@functionLog
def runPyBenchmark(python_path: str, ip: str):
    """run benchmark by import as python module

    Args:
        python_path (string): python benchmark script path
        ip (string): target ip address
    """
    suc, res = sysCommand("cp {} {}".format(
        python_path, os.path.join(Config.tmp_dir, 'benchmark.py')))
    if not suc:
        return False, "failed to copy benchmark script {} to {}".format(python_path, os.path.join(Config.tmp_dir, 'benchmark.py'))

    sys.path.append(Config.keentune_workspace)
    
    try:
        from tmplib.benchmark import Benchmark
    except ModuleNotFoundError as e:
        return False, "import benchmark failed:{}".format(e)
    else:
        return Benchmark(ip).run()
