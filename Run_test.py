import entity as en
from nornir.core.filter import F
import keyboard

import tests.Fortinet_FortiOS_HA_sync as has
import tests.Fortinet_FortiOS_adjacency as adj
import tests.Fortinet_FortiOS_unauthorize_acc as uac
import tests.Fortinet_FortiOS_firewall_test as fit
import tests.Fortinet_FortiOS_syslog as sys
import tests.Fortinet_FortiOS_IPS_test as ips
import tests.Fortinet_FortiOS_AV_test as avt
import tests.Fortinet_FortiOS_URLs_availability as uav
import tests.Fortinet_FortiOS_network_services as nes
import tests.Fortinet_FortiOS_URL_list_update as url
import tests.Fortinet_FortiOS_signatures_update as sup
import tests.Fortinet_FortiManager_device_list as mdl
import tests.Fortinet_FortiAnalyzer_device_list as adl
import tests.Fortinet_FortiAuthenticator_device_status as ads

def main ():
    nr = en.nrun()
    
    nr_fos = nr.filter(F(groups__contains="fortios"))
    devices_fos = en.get_devices(nr_fos)
    nr_fake = nr.filter(F(groups__contains="nofortios"))
    devices_fake = en.get_devices(nr_fake)
    #nr_local = nr.filter(F(groups__contains="pc"))
    #devices_local = en.get_devices(nr_local)
    nr_serv = nr.filter(F(groups__contains="pc_srv"))
    devices_serv = en.get_devices(nr_serv)
    nr_manager = nr.filter(F(groups__contains="manager"))
    devices_manager = en.get_devices(nr_manager)
    nr_analyzer = nr.filter(F(groups__contains="analyzer"))
    devices_analyzer = en.get_devices(nr_analyzer)
    nr_auth = nr.filter(F(groups__contains="auth"))
    devices_auth = en.get_devices(nr_auth)
    
    run_func(has, nr_fos, devices_fos) #1
    run_func(adj, nr_fos, devices_fos) #2
    run_func(uac, nr_fake, devices_fake) #3
    run_func(fit, nr_fos, devices_fos) #4
    run_func(sys, nr_fos, devices_fos) #5
    run_func(ips, nr_serv, devices_serv) #6
    run_func(avt, nr_serv, devices_serv) #7
    run_func(uav, nr_serv, devices_serv) #8
    run_func(nes, nr_fos, devices_fos) #9
    run_func(url, nr_fos, devices_fos) #10
    run_func(sup, nr_fos, devices_fos) #11
    run_func(mdl, nr_manager, devices_manager) #12
    run_func(adl, nr_analyzer, devices_analyzer) #13
    run_func(ads, nr_auth, devices_auth) #14
    return 0 

def run_func(T, nr, devices):
    keyboard.wait('space') 
    result = T.test(nr, devices)
    print(en.bcolors.HEADER + "Result: " + result + "\n" + en.bcolors.ENDC)
 
if __name__ == '__main__':
    main()

