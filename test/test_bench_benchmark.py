import unittest
import requests
import json

from common import bench_ip, bench_port, keentuned_ip, keentuned_port

class TestBenchBenchmark(unittest.TestCase):
    def setUp(self) -> None:
        self.proxies={"http": None, "https": None}
        url = "http://{}:{}/status".format(bench_ip, bench_port)
        re = requests.get(url, proxies=self.proxies)
        if re.status_code != 200:
            print("ERROR: Can't reach KeenTune-Bench.")
            exit()
            
        url = "http://{}:{}/{}".format(bench_ip, bench_port, "sendfile")
        data = {
            "file_name":"demo.sh",
            "encode_type":"utf-8",
            "body":"echo a=1"
            }

        headers = {"Content-Type": "application/json"}
        
        result = requests.post(url, data=json.dumps(data), headers=headers, proxies=self.proxies)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.text, '{"suc": true, "msg": "/var/keentune/files/demo.sh"}')
 
    def tearDown(self) -> None:
        pass

    def test_bench_server_FUN_benchmark(self):
        url = "http://{}:{}/{}".format(bench_ip, bench_port, "benchmark")
        data = {
            "bench_id": 1,
            "resp_ip": keentuned_ip,
            "resp_port": keentuned_port,
            "benchmark_cmd":"bash demo.sh"
        }

        headers = {"Content-Type": "application/json"}
        
        result = requests.post(url, data=json.dumps(data), headers=headers, proxies=self.proxies)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.text, '{"suc": true, "msg": ""}')
