# Node Protocol - CDP

## Filter CDP interface by local interface name

```
# iserver get aci proto cdp --apic apic11 --node rl --intf *1/4* --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-------------+------------+-------+--------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors          | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+--------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A | 62226   | 62219       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A | 61675   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+--------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node rl --intf *1/4* --view intf

{
    "duration": 3709,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 3179,
        "total_time": 3579
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	335	11	apic11o.emea-sp.cisco.com class fabricNode
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	297	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	1337	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	291	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	298	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)