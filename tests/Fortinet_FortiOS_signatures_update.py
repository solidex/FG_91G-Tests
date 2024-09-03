import yaml
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_signatures_update as T
from itertools import product

def test(nr, devices):
    categories = [
        "AV Engine", "Virus Definitions",
        "Mobile Malware Definitions", "IPS Attack Engine",
        "Attack Definitions", "Attack Extended Definitions", 
        "Industrial Attack Definitions", "Flow-based Virus Definitions",
        "Botnet Domain Database", "Internet-service Standard Database",
        "Malicious Certificate DB", "AntiPhish Pattern DB",
        "AI/Machine Learning Malware Detection Model"
    ]
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n11. Работоспособность сервиса обновления сигнатур вредоносного ПО,\nполучения сведений о категориях веб-сайтов:\n" + en.bcolors.ENDC)
    #results = en.send_commands(nr, "show webfilter urlfilter")
    mas = []
    results = en.send_commands(nr, "diag autoupdate versions")
    for i, j in product(devices, categories):
        try:
            mas = en.add_result_fw(results[i][0], i, j, mas, T)
        except:
            print(bcolors.WARNING + f"Отсутствует подключение к {i}" + bcolors.ENDC)
            mas.append("ERROR")
    #debug
    print(mas)
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