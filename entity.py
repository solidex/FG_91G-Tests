from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from nornir.core.filter import F
from tests import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def nrun ():
    return InitNornir(config_file="inventory/config.yaml")

def send_commands(nr, command):
    return nr.run(task=netmiko_send_command, command_string=command, read_timeout=50)

def get_devices(nr):
    mas = []
    for key in nr.inventory.hosts.keys():
        mas.append(key)
    return mas

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line)
            if line.split(" ")[-1] == "OK":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"

def check_answer(mas):
    for j in mas:
        if j != "OK":
            return "Fail"
    return "OK"

def add_result(results, devices, check_string, mas, T):
    for i in devices:
        print(bcolors.OKBLUE + i + bcolors.ENDC)
        try:
            dev = results[i][0]
            answ_dev = T.cut(dev, check_string)
            mas.append(answ_dev)
            if answ_dev == "ERROR":
                print(bcolors.WARNING + str(dev) + bcolors.ENDC)
                print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
                continue
        except:
            print(bcolors.WARNING + f"Отсутствует подключение к {i}" + bcolors.ENDC)
            answ_dev = "ERROR"
            mas.append(answ_dev)
    return mas

def get_device_api(nr, name):
    a = nr.inventory.dict()
    b = dict(list(a.values())[0])[name]['groups'][0]
    c = dict(list(a.values())[0])[name]['hostname']
    d = dict(list(a.values())[1])[b]['password']
    return [c, d]