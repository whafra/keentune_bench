import os
import json
import traceback

from tornado.web import RequestHandler

from bench.modules import benchmark
from bench.common.config import Config

from tornado.httpclient import HTTPClient, HTTPRequest, HTTPError
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from tornado.gen import coroutine

class BenchmarkHandler(RequestHandler):
    executor = ThreadPoolExecutor(20)

    @run_on_executor
    def _response(self,
                  response_data:dict,
                  response_ip  :str,
                  response_port:str):
        http_client = HTTPClient()
        try:
            response = http_client.fetch(HTTPRequest(
                url    = "http://{ip}:{port}/benchmark_result".format(
                            ip = response_ip, port = response_port),
                method = "POST",
                body   = json.dumps(response_data)
            ))
        except RuntimeError as e:
            return False, "{},{}".format(e, traceback.format_exc())

        except HTTPError as e:
            return False, "{},{}".format(e, traceback.format_exc())

        except Exception as e:
            return False, "{},{}".format(e, traceback.format_exc())

        else:
            if response.code == 200:
                return True, ""
            else:
                return False, response.reason

        finally:
            http_client.close()


    @run_on_executor
    def _runBenchmark(self, bench_cmd: str):
        def _parseBenchmarkResult(benchmark_result: str):
            benchmark_result_dict = {}
            for equation in benchmark_result.split(","):
                name = equation.split("=")[0].strip()
                value = equation.split("=")[1].strip()
                benchmark_result_dict[name] = {"value": float(value)}
            return True, benchmark_result_dict

        benchcmd_list = bench_cmd.split()
        benchcmd_list[1] = os.path.join(Config.FILES_PATH, benchcmd_list[1])
        bench_cmd_local = " ".join(benchcmd_list)

        suc, result = benchmark.runBenchmark(bench_cmd_local)
        if not suc:
            return False, result

        try:
            suc, benchmark_result_dict = _parseBenchmarkResult(benchmark_result=result)
            if not suc:
                return False, "parse benchmark result failed:{}".format(benchmark_result_dict)
        except IndexError as e:
            return False, "invalid output format of benchmark script: {}".format(e)
        
        return suc, benchmark_result_dict


    @coroutine
    def post(self):
        def _validField(request_data):
            assert request_data.__contains__('resp_ip')
            assert request_data.__contains__('resp_port')
            assert request_data.__contains__('benchmark_cmd')
            assert request_data.__contains__('bench_id')

        request_data = json.loads(self.request.body)
        try:
            _validField(request_data)
        
        except Exception as e:
            self.write(json.dumps({"suc" : False, "msg": str(e)}))
            self.finish()

        else:
            self.write(json.dumps({"suc" : True, "msg": ""}))
            self.finish()
            suc, res = yield self._runBenchmark(bench_cmd = request_data['benchmark_cmd'])
            if suc:
                response_data = {"suc": suc, "result": res, "msg": "", "bench_id": request_data['bench_id']}
            else:
                response_data = {"suc": suc, "result": {}, "msg": res, "bench_id": request_data['bench_id']}
            
            _, msg = yield self._response(response_data, request_data['resp_ip'], request_data['resp_port'])
            print(msg)
