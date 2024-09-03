import yaml
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_URL_list_update as T
from itertools import product

def test(nr, devices):
    categories = [
        "IPS Malicious URL Database", "URL Allow list"
    ]
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n10. Получение обновлений списков URL-фильтрации:\n" + en.bcolors.ENDC)
    results = en.send_commands(nr, "diag autoupdate versions")
    mas = []
    for i, j in product(devices, categories):
        try:
            mas = en.add_result_fw(results[i][0], i, j, mas, T)
        except:
            print(bcolors.WARNING + f"Отсутствует подключение к {i}" + bcolors.ENDC)
            mas.append("ERROR")
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