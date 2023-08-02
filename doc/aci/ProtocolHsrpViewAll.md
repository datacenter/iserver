# Node Protocol - HSRP

## All view

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view all
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Instance [#1]
-----------------------------

+---------------------+-------------+--------+---------+
| Node                | Admin State | Health | Faults  |
+---------------------+-------------+--------+---------+
| pod-1/cl201-eu-spdc | enabled     | 100    | 0 0 0 0 | 
+---------------------+-------------+--------+---------+

Protocol HSRP - Domain [#10]
----------------------------

+---------------------+-------------------------------+--------+---------+------------+
| Node                | VRF                           | Health | Faults  | Interfaces |
+---------------------+-------------------------------+--------+---------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 100    | 0 0 0 0 | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 100    | 0 0 0 0 | 0          | 
+---------------------+-------------------------------+--------+---------+------------+

Protocol HSRP - Interface [#0]
------------------------------
None

Protocol HSRP - Event Logs [#0]
-------------------------------
None

Protocol HSRP - Event Logs [#0]
-------------------------------
None

Protocol HSRP - Event Logs [#1]
-------------------------------

+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
| Node                | Sev  | Code     | Cause              | Created Time                  | Description                        | Affected                          |
+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
| pod-1/cl201-eu-spdc | Info | E4210476 | admin-state-change | 2023-05-31T23:11:11.462+02:00 | HSRP instance is administratively  | topology/pod-1/node-201/sys/hsrp/ | 
|                     |      |          |                    |                               | Enabled                            | inst-default                      | 
+---------------------+------+----------+--------------------+-------------------------------+------------------------------------+-----------------------------------+
```

Developer

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view all
    --when 90d

{
    "duration": 2886,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 2261,
        "total_time": 2647
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

True	386	-	connect apic11o.emea-sp.cisco.com:443
True	290	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query query-target=children&rsp-subtree-include=health,fault-count
True	322	10	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	266	0	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	319	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=faults,no-scoped,subtree
True	399	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	390	3	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolHsrp.md)