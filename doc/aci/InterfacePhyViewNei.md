# Node Interface - Physical

## CDP/LLDP focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view nei

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+--------------------+-----------------+--------------+-------------------------------+-------------------+
| Node                 | Interface | Oper | CDP System Name    | CDP Platform    | CDP Port ID  | LLDP System Name              | LLDP Port ID      |
+----------------------+-----------+------+--------------------+-----------------+--------------+-------------------------------+-------------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | FI-ucsb1-eu-spdc-A | UCS-FI-6454     | Ethernet1/53 | FI-ucsb1-eu-spdc-A.cisco.com  | Eth1/53           | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | FI-ucsb1-eu-spdc-B | UCS-FI-6454     | Ethernet1/53 | FI-ucsb1-eu-spdc-B.cisco.com  | Eth1/53           | 
| pod-1/bl2205-eu-spdc | 1/3       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/4       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/5       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/6       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/7       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/8       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/9       | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/10      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | HX1-eu-spdc-A      | UCS-FI-6454     | Ethernet1/53 | HX1-eu-spdc-A.cisco.com       | Eth1/53           | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | HX1-eu-spdc-B      | UCS-FI-6454     | Ethernet1/53 | HX1-eu-spdc-B.cisco.com       | Eth1/53           | 
| pod-1/bl2205-eu-spdc | 1/13      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/14      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/15      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/16      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/17      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/18      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/19      | up   |                    |                 |              | esx22-eu-spdc                 | 3c:fd:fe:e2:eb:68 | 
| pod-1/bl2205-eu-spdc | 1/20      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/21      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/22      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/23      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/24      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | ipn-eu-spdc        | N9K-C9504       | Ethernet3/27 | ipn-eu-spdc.emea-sp.cisco.com | Ethernet3/27      | 
| pod-1/bl2205-eu-spdc | 1/26      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | Yavin-129          | N9K-C93180YC-EX | Ethernet1/23 | Yavin-129                     | Ethernet1/23      | 
| pod-1/bl2205-eu-spdc | 1/28      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/29      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/30      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/31      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/32      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/33      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/34      | down |                    |                 |              |                               |                   | 
| pod-1/bl2205-eu-spdc | 1/35      | up   |                    |                 |              | s2101-eu-spdc.cisco.com       | Eth1/5            | 
| pod-1/bl2205-eu-spdc | 1/36      | up   |                    |                 |              | s2102-eu-spdc.cisco.com       | Eth1/5            | 
+----------------------+-----------+------+--------------------+-----------------+--------------+-------------------------------+-------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view nei

{
    "duration": 2980,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 2131,
        "total_time": 2531
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

True	400	-	connect apic21o.emea-sp.cisco.com:443
True	304	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	939	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	316	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	279	7	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	293	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
```

[[Back]](./InterfacePhy.md)