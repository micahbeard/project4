import port_scanner as port
from files_sysinfo import list_info as li
from check_perm import check


# View Files and Sys Info

def view_files():
    path = input("Enter Directory Path: ")
    li(path)


# port scanner
def nmap_scan():
    print("Type of Nmap scan")
    type_nmap = input("1: IP Scan \n2: IP + Port \n3: IP + Port -sS Scan \n4: Basic IP TCP Scan ")


    if type_nmap == '1':
        ip = input("What domain or IP: ")
        port.ip_scan(ip)
    elif type_nmap == '2':
        ip = input("What IP/Domain: ")
        port_nmap = input("Which port/ports: ")
        port.ports_scan(port_nmap,ip)
    elif type_nmap == '3':
        ip = input("What IP/Domian: ")
        port_nmap = input("Which port/ports: ")
        port.ss_scan(port_nmap,ip)
    elif type_nmap == '4':
        ip = input("What IP/Domain: ")
        port.common_scan(ip)

# check important files

def important():
    check()

loop = True
print("Welcome")
while loop:
    script = input("1: IP/Port scanner \n2: Important Directory Perms check \n3: List Files and System Enviroment \n4: Exit\n" )
    if script == "1":
        nmap_scan()
    elif script == "2":
        important()
    elif script == "3":
        view_files()
    else:
        loop = False

