from ping3 import ping
def ping_function():
    host=input("enter host: ")
    response=ping(host)

    if response is None:
        print("host is low:")
    else:
        print(f"response time : {response*1000:.2f} ms")

while True:
    print("1. Ping")
    print("2. Traceroute")
    choice = input("Choose option: ")



ping_function()