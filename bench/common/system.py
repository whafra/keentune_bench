import brain.controller
import subprocess
import os

from bench.common.pylog import functionLog
from bench.common.pylog import logger


@functionLog
def sysCommand(command: str, cwd: str = "./"):
    '''Run system command with subprocess.run and return result
    '''
    result = subprocess.run(
        command,
        shell=True,
        close_fds=True,
        cwd=cwd,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

    suc = (result.returncode == 0)
    out = result.stdout.decode('UTF-8', 'strict').strip()
    error = result.stderr.decode('UTF-8', 'strict').strip()

    if not suc:
        return suc, error
    else:
        return suc, out


def checkAddressAvaliable(address_list: list):
    result = {}
    for ip in address_list:
        suc, _ = sysCommand("ping -W 1 -c 1 {ip}".format(ip = ip))
        if not suc:
            logger.warning("Failed to ping {}".format(ip))
        else:
            logger.info("Success to ping {}".format(ip))
            
        result[ip] = suc
    return result

checkAddressAvaliable(["11.158.239.49"])