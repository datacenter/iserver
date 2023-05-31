# Node Interface - Management

## Single node

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/cl201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:15:14.143+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node cl201-eu-spdc

{
    "duration": 1869,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1291,
        "total_time": 1727
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

True	436	-	connect apic11o.emea-sp.cisco.com
True	338	11	apic11o.emea-sp.cisco.com class fabricNode
True	314	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)