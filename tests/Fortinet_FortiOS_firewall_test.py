import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_firewall_test as T

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n4. Работоспособность сервиса FW:\n" + en.bcolors.ENDC)
    mas = []
    nr_prod=nr[0].filter(name="Office_Prod_UTM")
    nr_inet=nr[0].filter(name="Office_Inet_UTM")
    serv = en.get_serv(nr[1])
    results = en.send_commands(nr_prod, f"exec ping {serv}")
    mas = en.add_result(results, [devices[0]], '5 packets transmitted, ', mas, T)
    results = en.send_commands(nr_inet, "exec ping www.google.com")
    mas = en.add_result(results, [devices[1]], '5 packets transmitted, ', mas, T)
    #debug
    #print(mas)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(lend[lend.index(line)-1])
            print(line)
            res = int(line.split(" ")[-3].split("%")[0])
            if res <= 20:
                print(lend[lend.index(line)+1])
                print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
                return "OK"
            else: 
                if res != 100:
                    print(lend[lend.index(line)+1])
                print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
                return "Fail" 
    return "ERROR"