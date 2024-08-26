import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_network_services as T

def test(nr, devices):
    mas = []
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n9. Доступность и работоспособность сервисов NTP и DNS:\n" + en.bcolors.ENDC)
    results = en.send_commands(nr, "get system ntp")
    mas = en.add_result(results, devices, 'ntpsync', mas, T)
    results = en.send_commands(nr, "get system dns")
    mas = en.add_result(results, devices, 'primary', mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line)
            if line.split(" ")[-2] == "enable":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
            if check_string == "primary" and line.split(" ")[-1] != "0.0.0.0":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    print (bcolors.WARNING + lend[0] + bcolors.ENDC)
    return "Fail"
    