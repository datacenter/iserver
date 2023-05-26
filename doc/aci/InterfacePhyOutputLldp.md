# Node Interface - Physical

## LLDP focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o lldp

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
| Node                | Interface | Oper | LLDP System Name              | Port ID           | Capability    | Mgmt IP       | Mgmt MAC          | State             |
+---------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | FI-ucsb1-eu-spdc-A.cisco.com  | Ethernet1/51      | bridge,router | 10.58.24.17   | 00:3A:9C:BD:92:40 | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/2       | up   | FI-ucsb1-eu-spdc-B.cisco.com  | Ethernet1/51      | bridge,router | 10.58.24.18   | 00:3A:9C:BD:8F:40 | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/3       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/4       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/5       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/6       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/7       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/8       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/9       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/10      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/11      | up   | HX1-eu-spdc-A.cisco.com       | Eth1/51           | bridge,router | 10.58.51.52   | 00:3A:9C:C0:04:80 | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/12      | up   | HX1-eu-spdc-B.cisco.com       | Eth1/51           | bridge,router | 10.58.51.53   | 00:3A:9C:C0:04:20 | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/13      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/14      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/15      | up   |                               | 3c:fd:fe:e2:f8:18 |               | unspecified   | unspecified       |                   | 
| pod-1/bl205-eu-spdc | 1/16      | up   |                               | 3c:fd:fe:e2:ee:d8 |               | unspecified   | unspecified       |                   | 
| pod-1/bl205-eu-spdc | 1/17      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/18      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/19      | up   |                               | 3c:fd:fe:e2:f4:f8 |               | unspecified   | unspecified       | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/20      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/21      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/22      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/23      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/24      | up   | ipn-eu-spdc.emea-sp.cisco.com | Ethernet3/25      | bridge,router | 10.58.234.128 | EC:CE:13:C0:46:34 |                   | 
| pod-1/bl205-eu-spdc | 1/25      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/26      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/27      | up   | Yavin-129                     | Ethernet1/21      | bridge,router | 10.58.244.129 | E0:0E:DA:A3:38:28 | portvlan-mismatch | 
| pod-1/bl205-eu-spdc | 1/28      | up   | Lisboa-54                     | TenGigE0/0/0/45   | router        | 15.16.2.1     | unspecified       |                   | 
| pod-1/bl205-eu-spdc | 1/29      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/30      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/31      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/32      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/33      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/34      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl205-eu-spdc | 1/35      | up   | s101-eu-spdc                  | Eth1/5            | bridge,router | 10.58.28.151  | unspecified       |                   | 
| pod-1/bl205-eu-spdc | 1/36      | up   | s102-eu-spdc                  | Eth1/5            | bridge,router | 10.58.28.152  | unspecified       |                   | 
+---------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
```

[[Back]](./InterfacePhy.md)