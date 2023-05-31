# Node Interface - Physical

## Filter by mac address

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --mac 8409

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:09 | trunk | 100G  | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --mac 8409

{
    "duration": 1665,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 1058,
        "total_time": 1468
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
    }
}

Log: apic
----------

True	410	-	connect apic11o.emea-sp.cisco.com
True	353	11	apic11o.emea-sp.cisco.com class fabricNode
True	328	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	377	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)