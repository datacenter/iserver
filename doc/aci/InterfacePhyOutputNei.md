# Node Interface - Physical

## CDP/LLDP focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o nei

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+--------------------+-----------------+-----------------+-------------------------------+-------------------+
| Node                | Interface | Oper | CDP System Name    | CDP Platform    | CDP Port ID     | LLDP System Name              | LLDP Port ID      |
+---------------------+-----------+------+--------------------+-----------------+-----------------+-------------------------------+-------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | FI-ucsb1-eu-spdc-A | UCS-FI-6454     | Ethernet1/51    | FI-ucsb1-eu-spdc-A.cisco.com  | Ethernet1/51      | 
| pod-1/bl205-eu-spdc | 1/2       | up   | FI-ucsb1-eu-spdc-B | UCS-FI-6454     | Ethernet1/51    | FI-ucsb1-eu-spdc-B.cisco.com  | Ethernet1/51      | 
| pod-1/bl205-eu-spdc | 1/3       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/4       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/5       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/6       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/7       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/8       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/9       | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/10      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/11      | up   | HX1-eu-spdc-A      | UCS-FI-6454     | Ethernet1/51    | HX1-eu-spdc-A.cisco.com       | Eth1/51           | 
| pod-1/bl205-eu-spdc | 1/12      | up   | HX1-eu-spdc-B      | UCS-FI-6454     | Ethernet1/51    | HX1-eu-spdc-B.cisco.com       | Eth1/51           | 
| pod-1/bl205-eu-spdc | 1/13      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/14      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/15      | up   |                    |                 |                 |                               | 3c:fd:fe:e2:f8:18 | 
| pod-1/bl205-eu-spdc | 1/16      | up   |                    |                 |                 |                               | 3c:fd:fe:e2:ee:d8 | 
| pod-1/bl205-eu-spdc | 1/17      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/18      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/19      | up   |                    |                 |                 |                               | 3c:fd:fe:e2:f4:f8 | 
| pod-1/bl205-eu-spdc | 1/20      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/21      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/22      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/23      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/24      | up   | ipn-eu-spdc        | N9K-C9504       | Ethernet3/25    | ipn-eu-spdc.emea-sp.cisco.com | Ethernet3/25      | 
| pod-1/bl205-eu-spdc | 1/25      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/26      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/27      | up   | Yavin-129          | N9K-C93180YC-EX | Ethernet1/21    | Yavin-129                     | Ethernet1/21      | 
| pod-1/bl205-eu-spdc | 1/28      | up   | Lisboa-54          | cisco NCS-5500  | TenGigE0/0/0/45 | Lisboa-54                     | TenGigE0/0/0/45   | 
| pod-1/bl205-eu-spdc | 1/29      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/30      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/31      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/32      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/33      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/34      | down |                    |                 |                 |                               |                   | 
| pod-1/bl205-eu-spdc | 1/35      | up   |                    |                 |                 | s101-eu-spdc                  | Eth1/5            | 
| pod-1/bl205-eu-spdc | 1/36      | up   |                    |                 |                 | s102-eu-spdc                  | Eth1/5            | 
+---------------------+-----------+------+--------------------+-----------------+-----------------+-------------------------------+-------------------+
```

[[Back]](./InterfacePhy.md)