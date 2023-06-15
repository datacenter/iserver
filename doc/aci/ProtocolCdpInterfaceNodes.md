# Node Protocol - CDP

## Show CDP interface counters for selected nodes

```
# iserver get aci proto cdp --apic apic11 --node rl --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors           | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 2751    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com | 2751    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A  | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc         | 2750    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+---------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --view intf

{
    "duration": 3795,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 579,
        "disconnect_time": 0,
        "mo_time": 2579,
        "total_time": 3158
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

True	579	-	connect apic11o.emea-sp.cisco.com
True	366	13	apic11o.emea-sp.cisco.com class fabricNode
True	455	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	332	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	377	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	355	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	353	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)