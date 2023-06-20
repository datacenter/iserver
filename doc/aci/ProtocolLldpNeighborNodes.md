# Node Protocol - LLDP

## Show LLDP neighbor for selected nodes

```
# iserver get aci proto lldp --apic apic11 --node bl --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| Node                | Interface ID | Hold Time | Neighbor Device               | MAC               | Port            | VLAN | Port Description                         | Capabilities  |
+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| pod-1/bl205-eu-spdc | eth1/35      | 120       | s101-eu-spdc                  | 4c:71:0d:55:d1:d1 | Eth1/5          |      | topology/pod-1/paths-101/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/36      | 120       | s102-eu-spdc                  | 8c:94:1f:fa:54:25 | Eth1/5          |      | topology/pod-1/paths-102/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com | 70:61:7b:d8:60:da | Ethernet1/27    | 12   | ***** BL-205-206 ACI1 Management *****   | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com  | 00:3a:9c:bd:92:40 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com  | 00:3a:9c:bd:8f:40 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com       | 00:3a:9c:c0:04:80 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com       | 00:3a:9c:c0:04:20 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/15      | 121       |                               | 3c:fd:fe:e2:f8:18 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/16      | 121       |                               | 3c:fd:fe:e2:ee:d8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/19      | 121       |                               | 3c:fd:fe:e2:f4:f8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com | ec:ce:13:c0:46:34 | Ethernet3/25    |      | ***** BGP Peering to ACI1 BL205  ******* | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/27      | 120       | Yavin-129                     | e0:0e:da:a3:38:28 | Ethernet1/21    | 1    | Ethernet1/21                             | bridge,router | 
| pod-1/bl205-eu-spdc | eth1/28      | 120       | Lisboa-54                     | 00:8a:96:1c:7c:de | TenGigE0/0/0/45 |      | *** Link to BL-205 for SR Handoff ***    | router        | 
| pod-1/bl206-eu-spdc | eth1/35      | 120       | s101-eu-spdc                  | 4c:71:0d:55:d1:d2 | Eth1/6          |      | topology/pod-1/paths-101/pathep-[eth1/6] | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/36      | 120       | s102-eu-spdc                  | 8c:94:1f:fa:54:26 | Eth1/6          |      | topology/pod-1/paths-102/pathep-[eth1/6] | bridge,router | 
| pod-1/bl206-eu-spdc | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com | 70:61:7b:d8:60:db | Ethernet1/28    | 12   | ***** BL-205-206 ACI1 Management *****   | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com  | 00:3a:9c:bd:92:44 | Eth1/52         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com  | 00:3a:9c:bd:8f:44 | Eth1/52         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com       | 00:3a:9c:c0:04:84 | Eth1/52         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com       | 00:3a:9c:c0:04:24 | Eth1/52         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com | cc:90:70:e6:96:28 | Ethernet2/25    |      | ***** BGP Peering to ACI1 BL206  ******* | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/27      | 120       | Yavin-129                     | e0:0e:da:a3:38:27 | Ethernet1/20    | 1    | Ethernet1/20                             | bridge,router | 
| pod-1/bl206-eu-spdc | eth1/28      | 120       | Lisboa-54                     | 00:8a:96:1c:7c:de | TenGigE0/0/0/44 |      | *** Link to BL-206 for SR Handoff ***    | router        | 
+---------------------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl --view nei

{
    "duration": 1824,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 640,
        "disconnect_time": 0,
        "mo_time": 1050,
        "total_time": 1690
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	640	-	connect apic11o.emea-sp.cisco.com:443
True	310	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	458	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	282	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)