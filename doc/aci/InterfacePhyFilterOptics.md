# Node Interface - Physical

## Filter by transceiver optics

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --optics xfp
    --view trans

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+----------+--------+---------------+------------+------------------+-----+-------------+
| Node                 | Interface | Oper | Present | State    | Optics | Name          | Type       | PN               | Rev | SN          |
+----------------------+-----------+------+---------+----------+--------+---------------+------------+------------------+-----+-------------+
| pod-1/bl2205-eu-spdc | 1/27      | up   | yes     | inserted | xfp    | CISCO-FINISAR | SFP-10G-LR | FTLX1474D3BCL-C2 | A   | FNS21090N2D | 
+----------------------+-----------+------+---------+----------+--------+---------------+------------+------------------+-----+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --optics xfp
    --view trans

{
    "duration": 2920,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 462,
        "disconnect_time": 0,
        "mo_time": 1986,
        "total_time": 2448
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

True	462	-	connect apic21o.emea-sp.cisco.com:443
True	348	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	979	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	330	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	329	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmFcot
```

[[Back]](./InterfacePhy.md)