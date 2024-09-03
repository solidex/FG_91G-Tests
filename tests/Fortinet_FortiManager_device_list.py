import entity as en
from entity import bcolors
import tests.Fortinet_FortiManager_device_list as T
import pyfortimanager


def test(nr, devices):   
    
    mas = []
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n12. Работоспособность ПО FortiManager:\n" + en.bcolors.ENDC)
    
    for i in devices:
        dev = en.get_device_api(nr, i)
        #print(dev)
        fortimanager = pyfortimanager.api(
            host = f"http://{dev[0]}",
            token = dev[1]
        )
        value = fortimanager.fortigates.all()
        results = list(value.values())[0]
        for j in range(0, len(results)):
            mas = add_result(results[j], devices, 'name', mas)
    return en.check_answer(mas)

def add_result(results, devices, check_string, mas):
    for i in devices:
        print(bcolors.OKBLUE + i + bcolors.ENDC)
        try:
            dev = results[check_string]
            if dev != "":
                print(dev)
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                mas.append("OK")
            else: 
                print(bcolors.WARNING + str(dev) + bcolors.ENDC)
                print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
                mas.append("Fail")
        except:
            print(bcolors.WARNING + f"Отсутствует подключение к {i}" + bcolors.ENDC)
            mas.append("ERROR")
    return mas

#diag dvm device list
#diag dvm device au
#TYPE            OID    SN               HA      IP              NAME              ADOM       MODE   FLAGS          
#unregistered    165    FEVM020000216145 -       172.17.17.245   FEVM020000216145  FortiMail  -                     
#unregistered    166    FG6H0FTB22901187 -       212.98.160.126  FG6H0FTB22901187  root       -            