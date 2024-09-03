import yaml
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_adjacency as T

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n2. IP-связность:\n" + en.bcolors.ENDC)
    with open("inventory/neighbours_inet.yaml", 'r') as stream:
        neighbours_inet = yaml.load(stream, Loader=yaml.SafeLoader)
    with open("inventory/neighbours_prod.yaml", 'r') as stream:
        neighbours_prod = yaml.load(stream, Loader=yaml.SafeLoader)
    mas = []
    nr_prod=nr.filter(name="Office_Prod_UTM")
    nr_inet=nr.filter(name="Office_Inet_UTM")
    for i in neighbours_prod:
        results = en.send_commands(nr_prod, f"exec ping {i}")
        mas = en.add_result(results, [devices[0]], '5 packets transmitted, ', mas, T)
    for i in neighbours_inet:
        results = en.send_commands(nr_inet, f"exec ping {i}")
        mas = en.add_result(results, [devices[1]], '5 packets transmitted, ', mas, T)
    #debug
    print(mas)
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