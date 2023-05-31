# Node Interface - Management

## Default state focused view

```
# iserver get aci intf mgmt --apic apic11 --node bl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:13:34.502+02:00 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:37:10.362+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node bl

{
    "duration": 2769,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 407,
        "disconnect_time": 0,
        "mo_time": 2229,
        "total_time": 2636
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

True	407	-	connect apic11o.emea-sp.cisco.com
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
True	320	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	345	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)