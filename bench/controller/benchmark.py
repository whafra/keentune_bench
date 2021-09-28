import os
import json

from tornado.web import RequestHandler

from bench.modules import benchmark
from bench.common.config import Config
from bench.common.pylog import APILog, functionLog
from bench.common.system import HTTPPost


class BenchmarkHandler(RequestHandler):
    async def post(self):
        request_data = json.loads(self.request.body)
        try:
            resp_ip = request_data['resp_ip']
            resp_port = request_data['resp_port']
            benchmark_cmd = request_data['benchmark_cmd']

        except KeyError as error_key:
            self.write(json.dumps({
                "suc": False,
                "msg": "can not find key: {}".format(error_key)
            }))
            self.finish()

        else:
            self.write(json.dumps({
                "suc": True,
                "msg": ""
            }))
            self.finish()

            suc, res = _runBenchmark(bench_cmd=benchmark_cmd)

            if suc:
                response_data = {
                    "suc": suc, "result": res, "msg": ""}
            else:
                response_data = {
                    "suc": suc, "result": "", "msg": res}

            await HTTPPost(
                api="benchmark_result",
                ip=resp_ip,
                port=resp_port,
                data=response_data
            )


@functionLog
def _parseBenchmarkResult(benchmark_result: str):
    benchmark_result_dict = {}
    for equation in benchmark_result.split(","):
        name = equation.split("=")[0].strip()
        value = equation.split("=")[1].strip()
        benchmark_result_dict[name] = {"value": float(value)}
    return True, benchmark_result_dict


@functionLog
def _runBenchmark(bench_cmd: str):
    benchcmd_list = bench_cmd.split()
    benchcmd_list[1] = os.path.join(Config.files_dir, benchcmd_list[1])
    bench_cmd_local = " ".join(benchcmd_list)

    suc, result = benchmark.runBenchmark(bench_cmd_local)
    if not suc:
        return False, result

    suc, benchmark_result_dict = _parseBenchmarkResult(benchmark_result=result)
    if not suc:
        return False, "parse benchmark result failed:{}".format(benchmark_result_dict)

    return suc, benchmark_result_dict
