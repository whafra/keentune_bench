from bench.common.system import sysCommand
from bench.common.pylog import functionLog


@functionLog
def runBenchmark(benchmark_cmd: str):
    """ run benchmark script.

    Try to import Benchmark class and call method Benchmark.run() if script is end with .py.

    Args:
        benchmark_cmd (str): run benchmark command.

    Returns:
        str: benchmark result or error message.
    """
    suc, res = sysCommand(benchmark_cmd)
    if suc:
        return True, res

    else:
        return False, "Execute the Benchmark script {} failed:{}".format(benchmark_cmd, res)