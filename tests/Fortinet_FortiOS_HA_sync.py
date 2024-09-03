import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_HA_sync as T

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n1. Синхронизация конфигураций узлов кластера:\n" + en.bcolors.ENDC)
    results = en.send_commands(nr, "get system ha status")
    mas = en.add_result(results, devices, 'Configuration Status:', [], T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line or line == "HA Health Status: OK":
            print(line)
            print(lend[lend.index(line)+1])
            print(lend[lend.index(line)+2])
            if lend[lend.index(line)+1].split(" ")[-1] == "in-sync" and lend[lend.index(line)+2].split(" ")[-1] == "in-sync":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"
