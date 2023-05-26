# Node Protocol - LLDP

## Verbose output

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc -o verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

LLDP Instance
-------------
- Admin State            : enabled
- Hold Time              : 120
- Init Delay Time        : 2
- Transmission Frequency : 30
- Neighbors              : 13


LLDP Instance Stats
-------------------
- Packets Sent        : 3032792
- Packets Received    : 3036197
- Packets Discarded   : 0
- Error Packets       : 0
- Adjacencies Added   : 26
- Adjacencies Removed : 0
- Entries Aged        : 0


+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| Node                | Interface ID | Hold Time | Neighbor Device               | MAC               | Port            | VLAN | Port Description                         | Capabilities  |
+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| pod-1/bl205-eu-spdc | eth1/35      | 120       | s101-eu-spdc                  | 4c:71:0d:55:d1:d1 | Eth1/5          |      | topology/pod-1/paths-101/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/36      | 120       | s102-eu-spdc                  | 8c:94:1f:fa:54:25 | Eth1/5          |      | topology/pod-1/paths-102/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com | 70:61:7b:d8:60:da | Ethernet1/27    | 12   | ***** BL-205-206 ACI1 Management *****   | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com  | 00:3a:9c:bd:92:40 | Ethernet1/51    | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com  | 00:3a:9c:bd:8f:40 | Ethernet1/51    | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com       | 00:3a:9c:c0:04:80 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com       | 00:3a:9c:c0:04:20 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/15      | 121       |                               | 3c:fd:fe:e2:f8:18 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/16      | 121       |                               | 3c:fd:fe:e2:ee:d8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/19      | 121       |                               | 3c:fd:fe:e2:f4:f8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com | ec:ce:13:c0:46:34 | Ethernet3/25    |      | ***** BGP Peering to ACI1 BL205  ******* | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/27      | 120       | Yavin-129                     | e0:0e:da:a3:38:28 | Ethernet1/21    | 1    | Ethernet1/21                             | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/28      | 120       | Lisboa-54                     | 00:8a:96:1c:7c:de | TenGigE0/0/0/45 |      | *** Link to BL-205 for SR Handoff ***    | router        | 
+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
```

[[Back]](./ProtocolLldp.md)