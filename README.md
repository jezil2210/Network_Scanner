<h1>Network Scanner</h1>

<p>Progam in python to verify hosts that are actives in some network</p>

<h2>Used Modules</h2>

<ul>
  <li>Scapy</li>
  <li>optparse</li>
</ul>

<h3>Scapy</h3>

<p>Scapy is a Python program that enables the user to send, sniff and dissect and forge network packets. Therefore with this module we can easely verify hosts connected to the same network with the function "arping()":</p>

<p>scapy.arping(192.168.1.0/24)</p>

<p>Although the goal of this repository is show how to do this deeply, so instead of using just the function "arping()" we will use the classes ARP and Ether from the module scapy to do the same thing. </p>
<p>so with the code below we firstly are gonna use scapy to create an ARP packet object and set the variable "pdst=ip", it's the ip range that i want to verify the hosts, (this ip is the ip that came like argument when the function is called). Then in the variable broadcast we use scapy.Ether with dst="ff:ff:ff:ff:ff:ff" to set the destination of this packet,in this case all hosts on the network, lastly but not least we use "scapy.srp()" to send the ARP packet and receive the response, and the variable answered_list to receive the response from the hosts</p>

<p>arp_request = scapy.ARP(pdst=ip)</p>
<p>broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")</p>
<p>arp_request_broadcast = broadcast/arp_request</p>
<p>answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]</p>

<p>it's used "[0]" like a list because the function "srp()" returns two list, one of answered responses and other of unanswered responses, and this case we need just the answered responses</p>

<p>The answered_list have more two elements, packet-sent, and answer, the packet-sent contains the ip and the MAC of the host that sent the packet, and the answer have the mac and the ip of the host that answered the ARP request </p>

<img src=image.png>

<p>The comma separates the information about the two elements(pack-sent, answer to ARP request) from the answered_list</p>





