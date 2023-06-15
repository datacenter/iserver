# Node Interface - Physical

## Filter by transceiver optics

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --optics xfp
    --view trans

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
| Node                | Interface | Oper | Present | State    | Optics | Name          | Type          | PN               | Rev  | SN            |
+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
| pod-1/bl205-eu-spdc | 1/27      | up   | yes     | inserted | xfp    | CISCO-AVAGO   | SFP-10G-LR    | SFCT-739SMZ      | G3.1 | AVD2047K5FA   | 
| pod-1/bl205-eu-spdc | 1/28      | up   | yes     | inserted | xfp    | CISCO-FINISAR | SFP-10G-AOC1M | FCBG110SD1C01-CS | A    | FIW205300M9-B | 
+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --optics xfp
    --view trans

{
    "duration": 1761,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1228,
        "total_time": 1627
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	309	13	apic11o.emea-sp.cisco.com class fabricNode
True	298	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	316	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	305	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmFcot
```

[[Back]](./InterfacePhy.md)