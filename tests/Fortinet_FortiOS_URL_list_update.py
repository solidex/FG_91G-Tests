import yaml
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_URL_list_update as T

def test(nr, devices):
    categories = [
        "IPS Malicious URL Database", "URL Allow list"
    ]
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n10. Получение обновлений списков URL-фильтрации:\n" + en.bcolors.ENDC)
    #results = en.send_commands(nr, "show webfilter urlfilter")
    results = en.send_commands(nr, "diag autoupdate versions")
    mas = []
    for i in categories:
        mas = en.add_result(results, devices, i, mas, T)
    #debug
    #print(mas)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line + "\n" + lend[lend.index(line)+2] + "\n" + lend[lend.index(line)+6])
            if lend[lend.index(line)+6] == 'Result: Updates Installed':
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
            else:               
                print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
                return "Fail" 
    return "ERROR"