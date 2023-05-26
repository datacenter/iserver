# Node Protocol - LLDP

## Show LLDP neighbors for all leaf nodes

```
# iserver get aci proto lldp --apic apic11 --role leaf -o nei

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-----------+---------------------------------+-------------------+---------------------+------+-----------------------------------------------+---------------+
| Node                | Interface ID | Hold Time | Neighbor Device                 | MAC               | Port                | VLAN | Port Description                              | Capabilities  |
+---------------------+--------------+-----------+---------------------------------+-------------------+---------------------+------+-----------------------------------------------+---------------+
| pod-1/bl205-eu-spdc | eth1/35      | 120       | s101-eu-spdc                    | 4c:71:0d:55:d1:d1 | Eth1/5              |      | topology/pod-1/paths-101/pathep-[eth1/5]      | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/36      | 120       | s102-eu-spdc                    | 8c:94:1f:fa:54:25 | Eth1/5              |      | topology/pod-1/paths-102/pathep-[eth1/5]      | bridge,router | 
| pod-1/bl205-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com   | 70:61:7b:d8:60:da | Ethernet1/27        | 12   | ***** BL-205-206 ACI1 Management *****        | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com    | 00:3a:9c:bd:92:40 | Ethernet1/51        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com    | 00:3a:9c:bd:8f:40 | Ethernet1/51        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com         | 00:3a:9c:c0:04:80 | Eth1/51             | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com         | 00:3a:9c:c0:04:20 | Eth1/51             | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/15      | 121       |                                 | 3c:fd:fe:e2:f8:18 |                     |      |                                               |               | 
| pod-1/bl205-eu-spdc | eth1/16      | 121       |                                 | 3c:fd:fe:e2:ee:d8 |                     |      |                                               |               | 
| pod-1/bl205-eu-spdc | eth1/19      | 121       |                                 | 3c:fd:fe:e2:f4:f8 |                     |      |                                               |               | 
| pod-1/bl205-eu-spdc | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com   | ec:ce:13:c0:46:34 | Ethernet3/25        |      | ***** BGP Peering to ACI1 BL205  *******      | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/27      | 120       | Yavin-129                       | e0:0e:da:a3:38:28 | Ethernet1/21        | 1    | Ethernet1/21                                  | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/28      | 120       | Lisboa-54                       | 00:8a:96:1c:7c:de | TenGigE0/0/0/45     |      | *** Link to BL-205 for SR Handoff ***         | router        | 
| pod-1/bl206-eu-spdc | eth1/35      | 120       | s101-eu-spdc                    | 4c:71:0d:55:d1:d2 | Eth1/6              |      | topology/pod-1/paths-101/pathep-[eth1/6]      | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/36      | 120       | s102-eu-spdc                    | 8c:94:1f:fa:54:26 | Eth1/6              |      | topology/pod-1/paths-102/pathep-[eth1/6]      | bridge,router | 
| pod-1/bl206-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com   | 70:61:7b:d8:60:db | Ethernet1/28        | 12   | ***** BL-205-206 ACI1 Management *****        | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com    | 00:3a:9c:bd:92:44 | Ethernet1/52        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com    | 00:3a:9c:bd:8f:44 | Ethernet1/52        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com         | 00:3a:9c:c0:04:84 | Eth1/52             | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com         | 00:3a:9c:c0:04:24 | Eth1/52             | 1    | U: Uplink                                     | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com   | cc:90:70:e6:96:28 | Ethernet2/25        |      | ***** BGP Peering to ACI1 BL206  *******      | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/27      | 120       | Yavin-129                       | e0:0e:da:a3:38:27 | Ethernet1/20        | 1    | Ethernet1/20                                  | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/28      | 120       | Lisboa-54                       | 00:8a:96:1c:7c:de | TenGigE0/0/0/44     |      | *** Link to BL-206 for SR Handoff ***         | router        | 
| pod-1/cl201-eu-spdc | eth1/107     | 120       | s101-eu-spdc                    | 4c:71:0d:55:d1:cd | Eth1/1              |      | topology/pod-1/paths-101/pathep-[eth1/1]      | bridge,router | 
| pod-1/cl201-eu-spdc | eth1/108     | 120       | s102-eu-spdc                    | 8c:94:1f:fa:54:21 | Eth1/1              |      | topology/pod-1/paths-102/pathep-[eth1/1]      | bridge,router | 
| pod-1/cl201-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com   | 70:61:7b:d8:60:d8 | Ethernet1/25        | 12   | ***** CL-201-201 ACI1 Management *****        | bridge,router | 
| pod-1/cl201-eu-spdc | eth1/1       | 121       |                                 | 3c:fd:fe:ce:13:a8 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/2       | 121       |                                 | 3c:fd:fe:ce:13:a9 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/3       | 121       |                                 | 3c:fd:fe:ce:13:aa |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/4       | 121       |                                 | 3c:fd:fe:cb:f5:b0 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/5       | 121       |                                 | 3c:fd:fe:cb:f5:b1 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/6       | 121       |                                 | 3c:fd:fe:cb:f5:b2 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/7       | 121       |                                 | 3c:fd:fe:ce:16:40 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/8       | 121       |                                 | 3c:fd:fe:ce:16:41 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/9       | 121       |                                 | 3c:fd:fe:ce:16:42 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/10      | 121       |                                 | 3c:fd:fe:ce:1a:60 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/11      | 121       |                                 | 3c:fd:fe:ce:1a:61 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/12      | 121       |                                 | 3c:fd:fe:ce:1a:62 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/13      | 121       |                                 | 3c:fd:fe:cb:ed:70 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/14      | 121       |                                 | 3c:fd:fe:cb:ed:71 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/15      | 121       |                                 | 3c:fd:fe:cb:ed:72 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/23      | 121       |                                 | 3c:fd:fe:ce:0e:40 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/49      | 121       |                                 | 3c:fd:fe:f0:15:10 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/50      | 121       |                                 | 3c:fd:fe:f0:15:11 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/51      | 121       |                                 | 3c:fd:fe:f0:15:12 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/52      | 121       |                                 | 40:a6:b7:08:fc:20 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/53      | 121       |                                 | 40:a6:b7:08:fc:21 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/54      | 121       |                                 | 40:a6:b7:08:fc:22 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/55      | 121       |                                 | 40:a6:b7:08:fc:28 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/56      | 121       |                                 | 40:a6:b7:08:fc:29 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/57      | 121       |                                 | 40:a6:b7:08:fc:2a |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/58      | 121       |                                 | 3c:fd:fe:f0:15:68 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/59      | 121       |                                 | 3c:fd:fe:f0:15:69 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/60      | 121       |                                 | 3c:fd:fe:f0:15:6a |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/61      | 121       |                                 | 3c:fd:fe:cb:f5:18 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/62      | 121       |                                 | 3c:fd:fe:cb:f5:19 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/63      | 121       |                                 | 3c:fd:fe:cb:f5:1a |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/64      | 121       |                                 | 3c:fd:fe:ce:c4:28 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/65      | 121       |                                 | 3c:fd:fe:ce:c4:29 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/66      | 121       |                                 | 3c:fd:fe:ce:c4:2a |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/67      | 121       |                                 | 3c:fd:fe:ef:6f:48 |                     |      |                                               |               | 
| pod-1/cl201-eu-spdc | eth1/81      | 120       | Napoli-45                       | e4:1f:7b:cf:a1:81 | TenGigE0/0/0/27.905 |      |                                               | router        | 
| pod-1/cl201-eu-spdc | eth1/91      | 120       | apic1                           | 5c:71:0d:ed:e4:0b |                     |      | eth2-1                                        |               | 
| pod-1/cl201-eu-spdc | eth1/92      | 120       | apic2                           | 5c:71:0d:ee:0c:4b |                     |      | eth2-1                                        |               | 
| pod-1/cl201-eu-spdc | eth1/93      | 120       | apic3                           | 5c:71:0d:ee:99:03 |                     |      | eth2-1                                        |               | 
| pod-1/cl201-eu-spdc | eth1/96      | 120       | ipn21-eu-spdc.emea-sp.cisco.com | 70:df:2f:d7:8a:07 | Ethernet1/48        | 1    | ***** Infra to ACI1 vPC *****                 | bridge,router | 
| pod-1/cl202-eu-spdc | eth1/107     | 120       | s101-eu-spdc                    | 4c:71:0d:55:d1:ce | Eth1/2              |      | topology/pod-1/paths-101/pathep-[eth1/2]      | bridge,router | 
| pod-1/cl202-eu-spdc | eth1/108     | 120       | s102-eu-spdc                    | 8c:94:1f:fa:54:22 | Eth1/2              |      | topology/pod-1/paths-102/pathep-[eth1/2]      | bridge,router | 
| pod-1/cl202-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com   | 70:61:7b:d8:60:d9 | Ethernet1/26        | 12   | ***** CL-201-201 ACI1 Management *****        | bridge,router | 
| pod-1/cl202-eu-spdc | eth1/1       | 121       |                                 | 3c:fd:fe:ce:16:48 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/2       | 121       |                                 | 3c:fd:fe:ce:16:49 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/3       | 121       |                                 | 3c:fd:fe:ce:16:4a |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/4       | 121       |                                 | 3c:fd:fe:cb:f5:e8 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/5       | 121       |                                 | 3c:fd:fe:cb:f5:e9 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/6       | 121       |                                 | 3c:fd:fe:cb:f5:ea |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/7       | 121       |                                 | 3c:fd:fe:ce:13:b8 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/8       | 121       |                                 | 3c:fd:fe:ce:13:b9 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/9       | 121       |                                 | 3c:fd:fe:ce:13:ba |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/10      | 121       |                                 | 3c:fd:fe:cb:f4:a8 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/11      | 121       |                                 | 3c:fd:fe:cb:f4:a9 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/12      | 121       |                                 | 3c:fd:fe:cb:f4:aa |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/13      | 121       |                                 | 3c:fd:fe:ce:0e:68 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/14      | 121       |                                 | 3c:fd:fe:ce:0e:69 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/15      | 121       |                                 | 3c:fd:fe:ce:0e:6a |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/23      | 121       |                                 | 3c:fd:fe:ce:11:b8 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/48      | 120       | rl401-eu-spdc                   | 34:73:2d:ea:4a:4a | Ethernet1/47        | 1    | Ethernet1/47                                  | bridge,router | 
| pod-1/cl202-eu-spdc | eth1/49      | 121       |                                 | 40:a6:b7:08:fc:48 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/50      | 121       |                                 | 40:a6:b7:08:fc:49 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/51      | 121       |                                 | 40:a6:b7:08:fc:4a |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/52      | 121       |                                 | 3c:fd:fe:f0:14:f8 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/53      | 121       |                                 | 3c:fd:fe:f0:14:f9 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/54      | 121       |                                 | 3c:fd:fe:f0:14:fa |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/55      | 121       |                                 | 40:a6:b7:0b:df:20 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/56      | 121       |                                 | 40:a6:b7:0b:df:21 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/57      | 121       |                                 | 40:a6:b7:0b:df:22 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/58      | 121       |                                 | 40:a6:b7:08:ec:88 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/59      | 121       |                                 | 40:a6:b7:08:ec:89 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/60      | 121       |                                 | 40:a6:b7:08:ec:8a |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/61      | 121       |                                 | 40:a6:b7:08:fb:b0 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/62      | 121       |                                 | 40:a6:b7:08:fb:b1 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/63      | 121       |                                 | 40:a6:b7:08:fb:b2 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/64      | 121       |                                 | 3c:fd:fe:cb:f7:68 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/65      | 121       |                                 | 3c:fd:fe:cb:f7:69 |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/66      | 121       |                                 | 3c:fd:fe:cb:f7:6a |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/67      | 121       |                                 | 3c:fd:fe:ef:6f:4b |                     |      |                                               |               | 
| pod-1/cl202-eu-spdc | eth1/91      | 120       | apic1                           | 5c:71:0d:ed:e4:0b |                     |      | eth2-2                                        |               | 
| pod-1/cl202-eu-spdc | eth1/92      | 120       | apic2                           | 5c:71:0d:ee:0c:4b |                     |      | eth2-2                                        |               | 
| pod-1/cl202-eu-spdc | eth1/93      | 120       | apic3                           | 5c:71:0d:ee:99:03 |                     |      | eth2-2                                        |               | 
| pod-1/cl202-eu-spdc | eth1/96      | 120       | ipn22-eu-spdc.emea-sp.cisco.com | 70:df:2f:96:e2:b7 | Ethernet1/48        | 1    | ***** Infra to ACI1 vPC *****                 | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/33      | 120       | rl302-eu-spdc                   | a0:b4:39:4a:2d:39 | Eth1/33             |      | topology/pod-1/paths-302/pathep-[eth1/33]     | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/34      | 120       | rl302-eu-spdc                   | a0:b4:39:4a:2d:3a | Eth1/34             |      | topology/pod-1/paths-302/pathep-[eth1/34]     | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/36      | 120       | Berlin-35.cisco.com             | 00:8a:96:9a:c0:e0 | TenGigE0/0/0/18     |      |                                               | router        | 
| pod-1/rl301-eu-spdc | mgmt0        | 120       | r23-eu-spdc.emea-sp.cisco.com   | c4:4d:84:a1:9e:68 | Ethernet1/41        | 12   | ***** rl301-eu-spdc mgmt0 *****               | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/26/1    | 180       | esx6-eu-spdc.cisco.com          | 3c:fd:fe:f0:3e:62 |                     |      | port 374 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/26/2    | 180       | esx7-eu-spdc.cisco.com          | 3c:fd:fe:ef:63:7b |                     |      | port 373 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/26/3    | 180       | esx8-eu-spdc.cisco.com          | 3c:fd:fe:cb:f5:13 |                     |      | port 371 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/26/4    | 180       | esx9-eu-spdc                    | 3c:fd:fe:cb:f5:53 |                     |      | port 849 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/24/1    | 180       | esx14-eu-spdc                   | 3c:fd:fe:cb:a5:6b |                     |      | port 986 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/24/2    | 180       | esx1-eu-spdc                    | 3c:fd:fe:cb:b0:03 |                     |      | port 988 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/25/1    | 180       | esx2-eu-spdc                    | 3c:fd:fe:ce:11:43 |                     |      | port 19 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge        | 
| pod-1/rl301-eu-spdc | eth1/25/2    | 180       | esx3-eu-spdc                    | 3c:fd:fe:ce:19:f3 |                     |      | port 1 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge        | 
| pod-1/rl301-eu-spdc | eth1/25/3    | 180       | esx4-eu-spdc                    | 3c:fd:fe:ce:1b:13 |                     |      | port 512 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge        | 
| pod-1/rl301-eu-spdc | eth1/25/4    | 180       | esx5-eu-spdc                    | 3c:fd:fe:cb:fa:9b |                     |      | port 257 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/27/1    | 180       | esx10-eu-spdc                   | 3c:fd:fe:cb:fa:43 |                     |      | port 853 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/27/2    | 180       | esx11-eu-spdc                   | 3c:fd:fe:cb:ec:eb |                     |      | port 851 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/27/3    | 180       | esx12-eu-spdc                   | 40:a6:b7:15:53:cb |                     |      | port 867 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/27/4    | 180       | esx13-eu-spdc                   | 3c:fd:fe:f0:13:0b |                     |      | port 865 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl301-eu-spdc | eth1/3       | 120       | FI-ucsb1-eu-spdc-B.cisco.com    | 00:3a:9c:bd:8f:35 | Ethernet1/46        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/4       | 120       | FI-ucsb1-eu-spdc-A.cisco.com    | 00:3a:9c:bd:92:35 | Ethernet1/46        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/rl301-eu-spdc | eth1/29      | 120       | Berlin-35.cisco.com             | 00:8a:96:9a:c0:e0 | TenGigE0/0/0/29     |      | *** Link to RL-301 for SR Handoff ***         | router        | 
| pod-1/rl302-eu-spdc | eth1/33      | 120       | rl301-eu-spdc                   | a0:b4:39:4a:2b:65 | Eth1/33             |      | topology/pod-1/paths-301/pathep-[eth1/33]     | bridge,router | 
| pod-1/rl302-eu-spdc | eth1/34      | 120       | rl301-eu-spdc                   | a0:b4:39:4a:2b:66 | Eth1/34             |      | topology/pod-1/paths-301/pathep-[eth1/34]     | bridge,router | 
| pod-1/rl302-eu-spdc | eth1/36      | 120       | Berlin-35.cisco.com             | 00:8a:96:9a:c0:e0 | TenGigE0/0/0/19     |      |                                               | router        | 
| pod-1/rl302-eu-spdc | mgmt0        | 120       | r23-eu-spdc.emea-sp.cisco.com   | c4:4d:84:a1:9e:69 | Ethernet1/42        | 12   | ***** rl302-eu-spdc mgmt0 *****               | bridge,router | 
| pod-1/rl302-eu-spdc | eth1/25/1    | 180       | esx2-eu-spdc                    | 3c:fd:fe:ce:11:42 |                     |      | port 18 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge        | 
| pod-1/rl302-eu-spdc | eth1/25/2    | 180       | esx3-eu-spdc                    | 3c:fd:fe:ce:19:f2 |                     |      | port 0 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge        | 
| pod-1/rl302-eu-spdc | eth1/25/3    | 180       | esx4-eu-spdc                    | 3c:fd:fe:ce:1b:12 |                     |      | port 513 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge        | 
| pod-1/rl302-eu-spdc | eth1/25/4    | 180       | esx5-eu-spdc                    | 3c:fd:fe:cb:fa:9a |                     |      | port 256 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/26/1    | 180       | esx6-eu-spdc.cisco.com          | 3c:fd:fe:f0:3e:63 |                     |      | port 375 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/26/2    | 180       | esx7-eu-spdc.cisco.com          | 3c:fd:fe:ef:63:7a |                     |      | port 372 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/26/3    | 180       | esx12-eu-spdc                   | 40:a6:b7:15:53:ca |                     |      | port 866 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/26/4    | 180       | esx13-eu-spdc                   | 3c:fd:fe:f0:13:0a |                     |      | port 864 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/24/1    | 180       | esx14-eu-spdc                   | 3c:fd:fe:cb:a5:6a |                     |      | port 987 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/24/2    | 180       | esx1-eu-spdc                    | 3c:fd:fe:cb:b0:02 |                     |      | port 989 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/27/1    | 180       | esx10-eu-spdc                   | 3c:fd:fe:cb:fa:42 |                     |      | port 852 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/27/2    | 180       | esx11-eu-spdc                   | 3c:fd:fe:cb:ec:ea |                     |      | port 850 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/27/3    | 180       | esx8-eu-spdc.cisco.com          | 3c:fd:fe:cb:f5:12 |                     |      | port 370 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/27/4    | 180       | esx9-eu-spdc                    | 3c:fd:fe:cb:f5:52 |                     |      | port 848 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge        | 
| pod-1/rl302-eu-spdc | eth1/3       | 120       | FI-ucsb1-eu-spdc-B.cisco.com    | 00:3a:9c:bd:8f:34 | Ethernet1/45        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/rl302-eu-spdc | eth1/4       | 120       | FI-ucsb1-eu-spdc-A.cisco.com    | 00:3a:9c:bd:92:34 | Ethernet1/45        | 1    | U: Uplink                                     | bridge,router | 
| pod-1/rl302-eu-spdc | eth1/29      | 120       | Berlin-35.cisco.com             | 00:8a:96:9a:c0:e0 | TenGigE0/0/0/28     |      | *** Link to RL-302 for SR Handoff ***         | router        | 
+---------------------+--------------+-----------+---------------------------------+-------------------+---------------------+------+-----------------------------------------------+---------------+
Interface context: lldp
```

[[Back]](./ProtocolLldp.md)