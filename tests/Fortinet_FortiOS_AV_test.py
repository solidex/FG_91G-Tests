import subprocess
import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_AV_test as T
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def test(nr, devices):
    #print(nr)
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n7. Работоспособность AV:\n" + en.bcolors.ENDC)
    mas = []
    serv = en.get_serv(nr)   
    results = subprocess.getoutput("curl -k https://secure.eicar.org/eicar.com")
    mas = en.add_result_fw(results, "Eicar.com", '    <p>You are not permitted to download the file', mas, T)
    results = subprocess.getoutput(f"curl {serv}")
    mas = en.add_result_fw(results, devices[0], '    <p>You are not permitted to download the file', mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line.split('<p>')[-1].split('</p>')[0])
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
            return "OK"
    print(lend[-1])
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"

#X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

#    <p>You are not permitted to download the file "eicar.com.txt" because it is infected with the virus "EICAR_TEST_FILE".</p>

#curl -k https://secure.eicar.org/eicar.com.txt