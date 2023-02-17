import os


def ip_scan(ip):
    os.system("sudo nmap "+ip)

def ports_scan(port, ip):
    print(f"Running nmap scan with IP:{ip} and ports:{port}")
    os.system(f'sudo nmap -p {port} {ip}')

def ss_scan(port, ip):
    print(f"Running a SYN “Half-open” Scans on {ip}, on port/ports{port}")
    os.system(f'sudo nmap -p {port} -sS {ip}')

def common_scan(ip):
    os.system(f'sudo nmap -sS {ip}')


def nmap_check():
    try:
        print("Checking if nmap is installed")
        os.system('sudo apt install nmap')
        
    
    except:
        print("Error With nmap")



