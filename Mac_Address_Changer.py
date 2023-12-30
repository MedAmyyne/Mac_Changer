import subprocess
import optparse
import pyfiglet
import re
import sys

def is_valid_mac(mac_address):
    return re.match(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$", mac_address) is not None

def Change_Mac(interface, new_mac):
    print("[<_>]  Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

def Get_Arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New Mac Address")
    options, _ = parser.parse_args()
    if not options.interface :
        parser.error("Please specify your interface, You can use --help for more information.")
    if not options.new_mac :
        parser.error("Please specify your new MAC address, You can use --help for more information.")
    if not is_valid_mac(options.new_mac):
        sys.exit("Invalid MAC address format. Please provide a valid MAC address.")
    return options

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("MaC'Hanger")
    print(ascii_banner)
    options = Get_Arguments()
    Change_Mac(options.interface, options.new_mac)
