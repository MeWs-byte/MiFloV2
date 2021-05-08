import socket



def whatsMyIp():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    mystring = f'Hi there!, you can find me @ http://{ip_address}:5000 !'
    print(mystring)
    #print(f'go to http://{ip_address}:5000')


if __name__=='__main__':
    whatsMyIp()
        