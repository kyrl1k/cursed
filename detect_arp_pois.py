import subprocess
import os
import time

while True:

        while True:
            subprocess.call("arp -a")
            get_output=subprocess.getoutput("arp -a")
            output_log =("Logs.txt", "w")
            output_log.write(get_output)
            output_log.close()
            log=open("Logs.txt","r")
            if log.mode == "r":
                contents=log.read()
                "мак адрес" in contents:
                    print("ARP заражение не обнаружено")
            elif "мак адрес" !=contents:
                    print("ARP заражение обнаружено")

