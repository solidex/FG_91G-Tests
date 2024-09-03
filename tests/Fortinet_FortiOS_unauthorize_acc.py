import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_unauthorize_acc as T

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n3. Управление доступом:\n" + en.bcolors.ENDC)
    results = en.send_commands(nr, "get system ha status")
    mas = en.add_result(results, devices, "Authentication to device failed.", [], T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line)
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
            return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"