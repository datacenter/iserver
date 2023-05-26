# Node Protocol - CDP

## Filter CDP neighbors by local interface name

```
# iserver get aci proto cdp --apic apic11 --node rl --intf *1/4*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------------+----------------------+-------------+--------------+--------+------+-------------+---------------------------------------+
| Node                | Local Interface | Neighbor System Name | Platform    | Port         | Duplex | MTU  | Native VLAN | Capabilities                          |
+---------------------+-----------------+----------------------+-------------+--------------+--------+------+-------------+---------------------------------------+
| pod-1/rl301-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454 | Ethernet1/46 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
| pod-1/rl302-eu-spdc | eth1/4          | FI-ucsb1-eu-spdc-A   | UCS-FI-6454 | Ethernet1/45 | full   | 9216 | 1           | igmp-filter,router,stp-dispute,switch | 
+---------------------+-----------------+----------------------+-------------+--------------+--------+------+-------------+---------------------------------------+
```

[[Back]](./ProtocolCdp.md)