# Node Interface - Port Channel (PC)

## Filter by port channel id

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name          | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po1 | pod-4a-br-API | up    | enabled   | up    |        | active    | 100        | 1            | 
+---------------------+-----+---------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1

{
    "duration": 2124,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 464,
        "disconnect_time": 0,
        "mo_time": 1444,
        "total_time": 1908
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

True	464	-	connect apic11o.emea-sp.cisco.com
True	320	11	apic11o.emea-sp.cisco.com class fabricNode
True	394	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	396	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	334	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)