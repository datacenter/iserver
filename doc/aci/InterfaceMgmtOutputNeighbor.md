# Node Interface - Management

## Neighbor (cdp/lldp) focused output

```
# iserver get aci intf mgmt --apic apic11 --node any -o nei

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

+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| Node                | Name  | Admin State | OperState | CDP - Platform | CDP - System Name | CDP - Port   | LLDP - System Name            | LLDP - Port  |
+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/27 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/27 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/28 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/28 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/25 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/25 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/26 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/26 | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/41 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/41 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/42 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/42 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/39 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/39 | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/40 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/40 | 
+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
```

[[Back]](./InterfaceMgmt.md)