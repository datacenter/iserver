# Node Protocol - LACP

## Show LACP interface for selected node

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id  | Name              | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view intf

{
    "duration": 4061,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 504,
        "disconnect_time": 0,
        "mo_time": 3049,
        "total_time": 3553
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

True	504	-	connect apic11o.emea-sp.cisco.com
True	362	11	apic11o.emea-sp.cisco.com class fabricNode
True	398	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	358	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	406	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)