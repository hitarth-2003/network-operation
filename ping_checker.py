from ping3 import ping
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

def netstat():
    print("--------------netstat---------------")
    pass

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
            pass
        case '3':
            pass
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


