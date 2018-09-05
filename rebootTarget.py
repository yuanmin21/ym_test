'''******************************************************************************
   Copyright (c) 2018 Marvell International Ltd. and its affiliates.
   All rights reserved.
   *
   If you received this File from Marvell and you have entered into a commercial
   license agreement (a "Commercial License") with Marvell, the File is licensed
   to you under the terms of the applicable Commercial License.
   ******************************************************************************'''

import telnetlib
import os
import time
import sys
import subprocess
#APC have a telnet interface. Given the the apc IP connect to it and connect
#usage: python rebootTarget.py <APC IP> <TARGET MACHINE IP>
#reboot target machine while checking uart connection
#sometimes uart connection doest not enumerate
#one or two reboots usually resolves.

try:
        APC_IP = sys.argv[1]
        APC_SLOT = sys.argv[2]
        TARGET_IP = sys.argv[3]
        SSH_ID = sys.argv[4]
        
except IndexError:
        sys.exit("rebootTarget.py <apc ip> <apc slot> <pc ip>")
        
print("APC IP: {}".format(APC_IP))
print("Reboot machine with IP: {}".format(TARGET_IP))
time.sleep(15)
for i in range(5):
        tn = telnetlib.Telnet(APC_IP)
        tn.read_until("Name :".encode('utf-8'))
        tn.write("apc\r".encode('utf-8'))
        tn.read_until(" :".encode('utf-8'))
        tn.write("apc\r".encode('utf-8'))
        tn.read_until("apc>".encode('utf-8'))
        tn.write("oldlyreboot {}\r".format(APC_SLOT).encode('utf-8'))
        tn.read_until("apc>".encode('utf-8'))
        tn.write("exit".encode('utf-8'))
        time.sleep(10) #wait a bit for apc to respond

        #now ping repeatedly until machine is rebooted
        proc = subprocess.Popen(["ping",TARGET_IP],stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=1,universal_newlines=True)

                        
        while True:
                output = proc.stdout.readline()
                if output == "" and proc.poll() is not None:
                        break
                if ("from {}".format(TARGET_IP) in output):
                        time.sleep(5)
                        print("Target is ready")
                        break
                else:
                        print("Pinging Target machine: " + output)
        
        proc.kill()
        time.sleep(20)
        break
##        proc = subprocess.Popen(["ssh",SSH_ID,"'lsusb'"],stdout=subprocess.PIPE)
##        out,err = proc.communicate()
##        if("UART" in str(out)):
##                print("UART found")
##                sys.stdout.flush()
##                sys.exit(0)
##        print("UART NOT FOUND RETRYING...")
##        sys.stdout.flush()
##sys.exit("UART NOT FOUND PHYSICAL INTERVENTION MIGHT BE NEEDED")

