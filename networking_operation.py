from ping3 import ping
import subprocess
import psutil


def ping_function():
    print("--------------------ping-------------------")
    host=input("enter host: ")
    response=ping(host)

    if response is None:
        print("host is low:")
    else:
        print(f"response time : {response*1000:.2f} ms")

def traceroute():
    print("--------------traceroute---------------")
    host=input("enter host:")
    result= subprocess.run(["tracert", host], capture_output=True, text=True)
    print(result.stdout)


    


def netstat():
    print("--------------netstat---------------")

    proto = input("enter protocol (tcp/udp/all: )").lower()
    
    
    connections = psutil.net_connections(kind='inet')
    
    print(f"{'Proto':<8} {'Local Address':<25} {'Remote Address':<25} {'Status':<15} {'PID'}")
    
    for conn in connections:
        
        protocol = "TCP" if conn.type == 1 else "UDP"
        
        if proto != "all" and proto.upper() != protocol:
            continue

        laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"

        print(f"{protocol:<8} {laddr:<25} {raddr:<25} {conn.status:<15} {conn.pid}")

def ifconfig():
    print("--------------ifconfig---------------")
    pass

def mtr():
    print("--------------mtr---------------")
    pass

def nslookup():
    print("--------------nslookup---------------")
    pass

def telnet():
    print("--------------telnet---------------")
    pass

def hostname():
    print("--------------hostname---------------")
    pass

def ip():
    print("--------------ip---------------")
    pass

def ipconfig():
    print("--------------ipconfig---------------")
    pass



while True:
    print("1. Ping\n")
    print("2. Traceroute\n")
    print("3. netstat\n")
    print("4. ifconfig\n") 
    print("5. mtr\n")
    print("6. nslookup\n")
    print("7. telnet\n")
    print("8. hostname\n")
    print("9. ip\n")
    print("10. 1wconfig\n")
    choice = input("Choose option: ")
    
    
    match choice:
        case '1':
            ping_function()
            break
        case '2':
            traceroute()
            break
        case '3':
            if __name__ == "__main__":
                netstat()
            break
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            pass
        case '9':
            pass
        case '10':
            pass
        case _:
            print("defaul:")


ff