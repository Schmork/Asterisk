from asterisk import manager
import time
import os
import threading

lastOneFinished = False

def worker(ident):
    """thread worker function"""
    if (ident == 0):
        response = m.originate(targetURL, 102, context='name-record', priority=1)
        print(m.status())
        lastOneFinished = False
    if (ident == 1):
        response2 = m.originate(targetURL_stephan, 102, context='name-record', priority=1)
        print(m.status())
        lastOneFinished = True
    return

HOST = '192.168.2.117'
PORT = 5038

inter_counter = 0

m = manager.Manager()
m.connect(HOST,port=PORT)

m.login('managerTest', 'ainesc')
targetURL = 'SIP/fonial/00497532808054'
targetURL_stephan = 'SIP/fonial2/004917696734058'

for i in range(2):
    if inter_counter == 0:
        response = m.originate(targetURL, 103, context='init-global-counter', priority=1, async=True)
        inter_counter += 1
        print ("Global var initiated")
    else:
        response = m.originate(targetURL_stephan, 102, context='name-record', priority=1, async=True)
        inter_counter += 1
    print(m.status())
#a += 1
#variables['key'] = str(a)
#response2 = m.originate(targetURL_stephan, 102, context='name-record', priority=1, async=True, variables=variables)
#print(m.status())
m.close()
