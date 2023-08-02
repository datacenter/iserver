# Node Interface - Loopback

## Default state output

```
# iserver get aci intf lb --apic apic21 --node bl2205-eu-spdc

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                 | Health | Faults  | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.66/32     | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.65/32     | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.232/32   | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 125.125.125.125/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo5       | up          | up         | 45.23.1.4/32       | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo6       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo7       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic21 --node bl2205-eu-spdc

{
    "duration": 2211,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 576,
        "disconnect_time": 0,
        "mo_time": 1305,
        "total_time": 1881
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

True	576	-	connect apic21o.emea-sp.cisco.com:443
True	429	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	400	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	476	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)