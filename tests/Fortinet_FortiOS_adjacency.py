import yaml
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_adjacency as T

def test(nr, devices):
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n2. IP-связность:\n" + en.bcolors.ENDC)
    with open("inventory/neighbours.yaml", 'r') as stream:
        neighbours = yaml.load(stream, Loader=yaml.SafeLoader)
    mas = []
    for i in neighbours:
        results = en.send_commands(nr, f"exec ping {i}")
        mas = en.add_result(results, devices, '5 packets transmitted, ', mas, T)
        #time.sleep(1)
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