import subprocess
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_URLs_availability as T
from nornir_netmiko.tasks import netmiko_send_command

def test(nr, devices):
    #print(nr)
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n8. Проверка работоспособности сервисов веб-фильтрации:\n" + en.bcolors.ENDC)
    mas = []
    serv = en.get_serv(nr)
    results = subprocess.getoutput("curl -k https://secure.eicar.org/eicar.com")
    mas = en.add_result_fw(results, "Eicar.com", 'URL Source: Local URLfilter Block', mas, T)
    results = subprocess.getoutput(f"curl {serv}")
    mas = en.add_result_fw(results, devices[0], 'URL Source: Local URLfilter Block', mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(check_string)
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
            return "OK"
    print(lend[-1])
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail" + bcolors.ENDC)
    return "Fail"

def add_result(results, devices, check_string, mas, T):
    for i in devices:
        print(bcolors.OKBLUE + i + bcolors.ENDC)
        try:
            dev = results[i][0]
            answ_dev = T.cut(dev, check_string)
            mas.append(answ_dev)
        except:
            print(bcolors.WARNING + f"curl: (56) Recv failure: Connection was reset" + bcolors.ENDC)
            answ_dev = "OK"
            mas.append(answ_dev)
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
    return mas


#X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

#    <p>You are not permitted to download the file "eicar.com.txt" because it is infected with the virus "EICAR_TEST_FILE".</p>

#curl -k https://secure.eicar.org/eicar.com.txt
#curl: (56) Recv failure: Connection was reset