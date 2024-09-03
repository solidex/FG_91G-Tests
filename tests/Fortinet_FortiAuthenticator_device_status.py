import entity as en
from entity import bcolors
import tests.Fortinet_FortiAuthenticator_device_status as T
from nornir_netmiko.tasks import netmiko_send_command

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n14. Работоспособность ПО FortiAuthenticator:\n" + en.bcolors.ENDC)
    mas = []
    results = en.send_commands(nr, "get system status")
    mas = en.add_result(results, devices, 'System:', mas, T)
    results = en.send_commands(nr, "diag net device")
    mas = en.add_result(results, devices, 'Inter', mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    #print(results)
    lend = str(results).splitlines()
    print(str(results).split("\n\nHA Status:")[0])
    for line in lend:
        if check_string in line:
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
            return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"
