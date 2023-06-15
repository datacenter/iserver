# Node Interface - Port Channel (PC)

## Filter by port channel id

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name                    | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po1 | pod1a-AIO-2-SAMX_PolGrp | up    | enabled   | up    |        | active    | 100        | 1            | 
+---------------------+-----+-------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node cl201-eu-spdc --id po1

{
    "duration": 2236,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 685,
        "disconnect_time": 0,
        "mo_time": 1376,
        "total_time": 2061
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

True	685	-	connect apic11o.emea-sp.cisco.com
True	335	13	apic11o.emea-sp.cisco.com class fabricNode
True	454	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	289	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	298	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)