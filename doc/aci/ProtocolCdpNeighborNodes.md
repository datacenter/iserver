# Node Protocol - CDP

## Show CDP neighbors details for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl -o nbr

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name | Platform       | Port            | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
| pod-1/rl301-eu-spdc | eth1/29         | Berlin-35.cisco.com  | cisco NCS-5500 | TenGigE0/0/0/29 | full   | 0    |             | router                                | 
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/46    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl301-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/41    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/29         | Berlin-35.cisco.com  | cisco NCS-5500 | TenGigE0/0/0/28 | full   | 0    |             | router                                | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454    | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/3          | FI-ucsb1-eu-spdc-B   | UCS-FI-6454    | Ethernet1/45    | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | mgmt0           | r23-eu-spdc          | N9K-C92348GC-X | Ethernet1/42    | full   | 1500 | 12          | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+----------------------+----------------+-----------------+--------+------+-------------+---------------------------------------+
```

[[Back]](./ProtocolCdp.md)