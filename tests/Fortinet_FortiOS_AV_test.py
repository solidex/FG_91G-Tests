import entity as en
from entity import bcolors
import tests.Fortinet_FortiOS_AV_test as T
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def test(nr, devices):
    #print(nr)
    print(en.bcolors.UNDERLINE + en.bcolors.BOLD + "\n7. Работоспособность AV:\n" + en.bcolors.ENDC)
    mas = []
    results = en.send_commands(nr, "curl -k https://secure.eicar.org/eicar.com")
    mas = en.add_result(results, devices, '    <p>You are not permitted to download the file', mas, T)
    results = nr.run(task=netmiko_send_command, command_string=f"curl http://172.17.17.112", read_timeout=50)
    mas = en.add_result(results, devices, '    <p>You are not permitted to download the file', mas, T)
    return en.check_answer(mas)

def cut(results, check_string):
    lend = str(results).splitlines()
    for line in lend:
        if check_string in line:
            print(line.split('<p>')[-1].split('</p>')[0])
            print(bcolors.BOLD + "Check: " + bcolors.OKGREEN + "OK" + bcolors.ENDC)
            return "OK"
    print(lend[1])
    print(bcolors.BOLD + "Check: " + bcolors.FAIL + "Fail")
    return "Fail"


#X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

#    <p>You are not permitted to download the file "eicar.com.txt" because it is infected with the virus "EICAR_TEST_FILE".</p>

#curl -k https://secure.eicar.org/eicar.com.txt