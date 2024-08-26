import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_syslog as T

def test(nr, devices):
    mas = []
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n5. Отправка сообщений о событиях по протоколу Syslog:\n" + en.bcolors.ENDC)
    results = en.send_commands(nr, "get log syslogd setting")
    mas = en.add_result(results, devices, 'status', mas, T)
    results = en.send_commands(nr, "diag log test")
    #1: generating
    mas = en.add_result(results, devices, "1: generating", mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line)
            if line.split(" ")[-2] == "enable":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
            if check_string == "1: generating":
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"
