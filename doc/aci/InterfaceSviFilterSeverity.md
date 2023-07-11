# Node Interface - SVI

## Filter by severity

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --severity major
    --when 180d
    --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI Faults [#0]
-------------------------
None

Interface SVI Fault Records last 180d [#42]
-------------------------------------------

+----------------------+-----------+-----+-------+--------------------+-------------------------------+------------------+--------------------------------------------------------------------+
| Node                 | Interface | Sev | Code  | Cause              | Created Time                  | Lifecycle        | Description                                                        |
+----------------------+-----------+-----+-------+--------------------+-------------------------------+------------------+--------------------------------------------------------------------+
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:06:10.110+02:00 | soaking          | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:06:35.769+02:00 | soaking-clearing | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:06:59.812+02:00 | soaking          | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:07:11.620+02:00 | soaking-clearing | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:26:11.373+02:00 | soaking          | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:26:24.225+02:00 | soaking-clearing | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:44:07.307+02:00 | soaking          | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:46:33.398+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:48:24.111+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:48:52.076+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:49:04.224+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:51:31.583+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:51:50.438+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:52:11.055+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:52:22.972+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:53:42.998+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:54:01.340+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:54:22.178+02:00 | raised           | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan2     | Maj | F1224 | interface-svi-down | 2023-03-02T16:54:33.978+02:00 | raised-clearing  | SVI is down for 2 with operational state qualifier: vlan is down.  | 
| pod-1/cl2208-eu-spdc | vlan26    | Maj | F1224 | interface-svi-down | 2023-03-02T21:24:55.665+02:00 | soaking          | SVI is down for 26 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan26    | Maj | F1224 | interface-svi-down | 2023-03-02T21:26:59.460+02:00 | soaking-clearing | SVI is down for 26 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan26    | Maj | F1224 | interface-svi-down | 2023-04-12T18:25:03.850+02:00 | soaking          | SVI is down for 26 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan26    | Maj | F1224 | interface-svi-down | 2023-04-12T18:27:24.236+02:00 | raised           | SVI is down for 26 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan35    | Maj | F1224 | interface-svi-down | 2023-05-25T18:30:46.876+02:00 | soaking-clearing | SVI is down for 35 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan35    | Maj | F1224 | interface-svi-down | 2023-05-25T18:30:46.826+02:00 | soaking          | SVI is down for 35 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-05-31T22:20:44.547+02:00 | soaking          | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-05-31T22:23:05.482+02:00 | raised           | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T18:32:31.529+02:00 | raised-clearing  | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T18:32:52.935+02:00 | raised           | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T18:33:05.213+02:00 | raised-clearing  | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:10:21.282+02:00 | soaking          | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:10:33.101+02:00 | soaking-clearing | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:11:50.421+02:00 | soaking          | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:12:07.881+02:00 | soaking-clearing | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:12:32.371+02:00 | soaking          | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-04T19:12:44.184+02:00 | soaking-clearing | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-07T17:02:54.421+02:00 | soaking          | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan31    | Maj | F1224 | interface-svi-down | 2023-06-07T17:04:56.541+02:00 | raised           | SVI is down for 31 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan26    | Maj | F1224 | interface-svi-down | 2023-06-12T11:31:29.637+02:00 | soaking-clearing | SVI is down for 26 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan25    | Maj | F1224 | interface-svi-down | 2023-06-18T09:15:12.259+02:00 | soaking          | SVI is down for 25 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan25    | Maj | F1224 | interface-svi-down | 2023-06-18T09:17:30.913+02:00 | raised           | SVI is down for 25 with operational state qualifier: vlan is down. | 
| pod-1/cl2208-eu-spdc | vlan25    | Maj | F1224 | interface-svi-down | 2023-06-18T09:18:02.651+02:00 | raised-clearing  | SVI is down for 25 with operational state qualifier: vlan is down. | 
+----------------------+-----------+-----+-------+--------------------+-------------------------------+------------------+--------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf svi
    --apic apic21
    --node cl2208-eu-spdc
    --severity major
    --when 180d
    --view fault

{
    "duration": 3548,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 2738,
        "total_time": 3136
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

True	398	-	connect apic21o.emea-sp.cisco.com:443
True	307	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	422	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	288	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	1721	248	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=faults,fault-records,no-scoped,subtree
```

[[Back]](./InterfaceSvi.md)