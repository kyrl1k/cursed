import os
def enable():
    os.system("netsh interface set interface 'Wifi' enabled")

def disable():
    os.system("netsh interface set interface 'Wifi' disabled")