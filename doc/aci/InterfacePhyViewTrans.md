# Node Interface - Physical

## Transceiver focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view trans

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
| Node                 | Interface | Oper | Present | State    | Optics  | Name            | Type            | PN               | Rev  | SN            |
+----------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | yes     | inserted | qsfp28  | CISCO-DELTA     | QSFP-100G-AOC3M | QAOC-100G4F1A03C | A    | DTS2418A796-B | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | yes     | inserted | qsfp28  | CISCO-DELTA     | QSFP-100G-AOC3M | QAOC-100G4F1A03C | A    | DTS2352A330-B | 
| pod-1/bl2205-eu-spdc | 1/3       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/4       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/5       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/6       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/7       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/8       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/9       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/10      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D    | FIW213402UA-B | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D    | FIW2134024Q-B | 
| pod-1/bl2205-eu-spdc | 1/13      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/14      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/15      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/16      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/17      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/18      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D    | FIW213402T9-B | 
| pod-1/bl2205-eu-spdc | 1/20      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/21      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/22      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/23      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/24      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | yes     | inserted | qsfp28  | CISCO-INNOLIGHT | QSFP-100G-AOC3M | TF-FC003-NC2     | 1B   | INL24358598-A | 
| pod-1/bl2205-eu-spdc | 1/26      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | yes     | inserted | xfp     | CISCO-FINISAR   | SFP-10G-LR      | FTLX1474D3BCL-C2 | A    | FNS21090N2D   | 
| pod-1/bl2205-eu-spdc | 1/28      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/29      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/30      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/31      | down | yes     | inserted | qsfp28  | CISCO-AVAGO     | QSFP-100G-SR4-S | SFBR-89CDDZ-CS5  | 06Bh | AVF2247S1EZ   | 
| pod-1/bl2205-eu-spdc | 1/32      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/33      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/34      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | no      | removed  | unknown |                 |                 |                  |      |               | 
+----------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view trans

{
    "duration": 3348,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 524,
        "disconnect_time": 0,
        "mo_time": 2204,
        "total_time": 2728
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

True	524	-	connect apic21o.emea-sp.cisco.com:443
True	332	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1029	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	471	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	372	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmFcot
```

[[Back]](./InterfacePhy.md)