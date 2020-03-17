#!/usr/bin/env python3

import scapy.all as scapy
import optparse

parser = optparse.OptionParser()
parser.add_option("-p","--iprange",dest="ip",help="ip range")

(options, arguments) = parser.parse_args()

if not options.ip:
   parser.error("Please specify an ip range to scan")
else:
   ipRange = options.ip

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for elements in answered_list:
        client_dict = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan(ipRange)
print_result(scan_result)
