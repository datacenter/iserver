# Node Protocol - CDP

## Show CDP interface counters for selected node

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 62227   | 58912       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 61869   | 61860       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 62213   | 62205       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 62215   | 62207       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 62166   | 62108       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 62227   | 62227       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 62227   | 62223       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view intf

{
    "duration": 2319,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 1796,
        "total_time": 2200
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

True	404	-	connect apic11o.emea-sp.cisco.com
True	435	11	apic11o.emea-sp.cisco.com class fabricNode
True	499	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	382	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	480	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)