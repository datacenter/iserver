# Node Protocol - CDP

## Show CDP neighbors details for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node any -o nbr

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name   | Platform        | Port            | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/2          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/11         | HX1-eu-spdc-A          | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/12         | HX1-eu-spdc-B          | UCS-FI-6454     | Ethernet1/51    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/28         | Lisboa-54              | cisco NCS-5500  | TenGigE0/0/0/45 | full   | 0    |             | router                                | 
| pod-1/bl205-eu-spdc | eth1/27         | Yavin-129              | N9K-C93180YC-EX | Ethernet1/21    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl205-eu-spdc | eth1/24         | ipn-eu-spdc            | N9K-C9504       | Ethernet3/25    | full   | 9216 |             | router,stp-dispute,switch             | 
| pod-1/bl205-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/27    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/1          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/2          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/11         | HX1-eu-spdc-A          | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/12         | HX1-eu-spdc-B          | UCS-FI-6454     | Ethernet1/52    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/28         | Lisboa-54              | cisco NCS-5500  | TenGigE0/0/0/44 | full   | 0    |             | router                                | 
| pod-1/bl206-eu-spdc | eth1/27         | Yavin-129              | N9K-C93180YC-EX | Ethernet1/20    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/bl206-eu-spdc | eth1/24         | ipn-eu-spdc            | N9K-C9504       | Ethernet2/25    | full   | 9216 |             | router,stp-dispute,switch             | 
| pod-1/bl206-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/28    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl201-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi     | vmnic4          | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/38         | esx10-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/37         | esx11-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/36         | esx12-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/35         | esx13-eu-spdc          | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/34         | esx14-eu-spdc          | VMware ESXi     | vmnic5          | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/39         | esx9-eu-spdc           | VMware ESXi     | vmnic10         | full   | 9000 |             | switch                                | 
| pod-1/cl201-eu-spdc | eth1/96         | ipn21-eu-spdc          | N9K-C93180YC-EX | Ethernet1/48    | full   | 1500 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl201-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/25    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl202-eu-spdc | eth1/41         | esx1-eu-spdc           | VMware ESXi     | vmnic5          | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/38         | esx10-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/37         | esx11-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/35         | esx13-eu-spdc          | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/34         | esx14-eu-spdc          | VMware ESXi     | vmnic4          | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/42         | esx2-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/43         | esx3-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/44         | esx4-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/45         | esx5-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/46         | esx6-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/47         | esx7-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/40         | esx8-eu-spdc.cisco.com | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/39         | esx9-eu-spdc           | VMware ESXi     | vmnic11         | full   | 9000 |             | switch                                | 
| pod-1/cl202-eu-spdc | eth1/96         | ipn22-eu-spdc          | N9K-C93180YC-EX | Ethernet1/48    | full   | 1500 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/cl202-eu-spdc | mgmt0           | r22-eu-spdc            | N9K-C92348GC-X  | Ethernet1/26    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/29         | Berlin-35.cisco.com    | cisco NCS-5500  | TenGigE0/0/0/29 | full   | 0    |             | router                                | 
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/41    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/29         | Berlin-35.cisco.com    | cisco NCS-5500  | TenGigE0/0/0/28 | full   | 0    |             | router                                | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A     | UCS-FI-6454     | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B     | UCS-FI-6454     | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/42    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/s101-eu-spdc  | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/39    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/s102-eu-spdc  | mgmt0           | r23-eu-spdc            | N9K-C92348GC-X  | Ethernet1/40    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+------------------------+-----------------+-----------------+--------+------+-------------+---------------------------------------+
```

[[Back]](./ProtocolCdp.md)