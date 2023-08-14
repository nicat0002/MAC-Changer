#MAC UNVAN DEYISHME TOOL-U
import subprocess
import optparse
import re

interface=''
macadress=''

def komekci_funk():
    parser=optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help="Bu funksiyalar Interfeysi sechmek uchundur")
    parser.add_option('-m','--mac',dest='macadress',help="Bu funksiyalar MAC-unvani sechmek uchundur")
    return parser.parse_args()


def komandalar(interface,macadress):
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw','ether',macadress])
    subprocess.call(['ifconfig',interface,'up'])

def inputu_yoxlama(interface,macadress):
    if not interface:
        interface=input("Interfeys-i faxil edin: ")
    if not macadress:
        macadress=input("MAC unvan-i daxil edin: ")
        return interface,macadress

def mac_yoxlama(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    ifcon_str=ifconfig.decode()
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifcon_str)
    if new_mac:
        return new_mac.group(0)
    else:
       return False


print("""
                                                               
 ( ' )                 (       )                                 
 )\))(      )         )\   ( /(     )         (  (     (   (    
((_)()\  ( /(   (   (((_)  )\()) ( /(   (     )\))(   ))\  )(   
(_()((_) )(_))  )\  )\___ ((_)\  )(_))  )\ ) ((_))\  /((_)(()\  
|  \/  |((_)_  ((_)((/ __|| |(_)((_)_  _(_/(  (()(_)(_))   ((_) 
| |\/| |/ _` |/ _|  | (__ | ' \ / _` || ' \))/ _` | / -_) | '_| 
|_|  |_|\__,_|\__|   \___||_||_|\__,_||_||_| \__, | \___| |_|   
                                             |___/              
                                            BY: NICAT ABBASOV
""")
(user_inputs,arg)=komekci_funk()
interface,macadress=inputu_yoxlama(user_inputs.interface,user_inputs.macadress)
komandalar(interface,macadress)
final_mac=mac_yoxlama(interface)
if final_mac==macadress:
     print("MAC unvani ugurla deyishdirildi")
else:
     print("Xeta bash verdi")

komandalar(interface,macadress)
