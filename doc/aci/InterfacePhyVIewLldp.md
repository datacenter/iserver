# Node Interface - Physical

## LLDP focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view lldp

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
| Node                 | Interface | Oper | LLDP System Name              | Port ID           | Capability    | Mgmt IP       | Mgmt MAC          | State             |
+----------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | FI-ucsb1-eu-spdc-A.cisco.com  | Eth1/53           | bridge,router | 10.58.24.17   | 00:3A:9C:BD:92:48 | portvlan-mismatch | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | FI-ucsb1-eu-spdc-B.cisco.com  | Eth1/53           | bridge,router | 10.58.24.18   | 00:3A:9C:BD:8F:48 | portvlan-mismatch | 
| pod-1/bl2205-eu-spdc | 1/3       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/4       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/5       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/6       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/7       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/8       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/9       | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/10      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | HX1-eu-spdc-A.cisco.com       | Eth1/53           | bridge,router | 10.58.51.52   | 00:3A:9C:C0:04:88 | portvlan-mismatch | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | HX1-eu-spdc-B.cisco.com       | Eth1/53           | bridge,router | 10.58.51.53   | 00:3A:9C:C0:04:28 | portvlan-mismatch | 
| pod-1/bl2205-eu-spdc | 1/13      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/14      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/15      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/16      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/17      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/18      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | esx22-eu-spdc                 | 3c:fd:fe:e2:eb:68 | bridge        | unspecified   | unspecified       |                   | 
| pod-1/bl2205-eu-spdc | 1/20      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/21      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/22      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/23      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/24      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | ipn-eu-spdc.emea-sp.cisco.com | Ethernet3/27      | bridge,router | 10.58.234.128 | EC:CE:13:C0:46:3C |                   | 
| pod-1/bl2205-eu-spdc | 1/26      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | Yavin-129                     | Ethernet1/23      | bridge,router | 10.58.244.129 | E0:0E:DA:A3:38:2A | portvlan-mismatch | 
| pod-1/bl2205-eu-spdc | 1/28      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/29      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/30      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/31      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/32      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/33      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/34      | down |                               |                   |               |               |                   |                   | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | s2101-eu-spdc.cisco.com       | Eth1/5            | bridge,router | 10.58.50.151  | unspecified       |                   | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | s2102-eu-spdc.cisco.com       | Eth1/5            | bridge,router | 10.58.50.152  | unspecified       |                   | 
+----------------------+-----------+------+-------------------------------+-------------------+---------------+---------------+-------------------+-------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view lldp

{
    "duration": 2949,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 1895,
        "total_time": 2311
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

True	416	-	connect apic21o.emea-sp.cisco.com:443
True	327	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	948	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	307	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
```

[[Back]](./InterfacePhy.md)